'''
Previous set-tup

! pip install diffusers transformers accelerate scipy safetensors
! mkdir products
! pip install openai==0.28

'''

import os
import random

# For text generation
import re
import openai
import pandas as pd
import api_key

# For background image generation
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# For image manipulation
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# --------------------------------------------------------------------------------------------------

def text_generation(place, products):
  openai.api_key = api_key.OPENAI_API_KEY
  responses = []
  n = 0

  df = pd.read_csv("promotion.csv", encoding="ISO-8859-1")
  env_rules_df = pd.read_csv("env_rules.csv", encoding="latin")
  env_rules_dict = env_rules_df.to_dict()

  Entorno = place#'Tienda'
  Products = products#['Coca Cola 600ml', 'Leche Santa Clara Light 1L', 'Garrafon Ciel 5L']

  content1 = Entorno
  content2 = ", ".join(Products)

  anuncio = [
      {"role": "system", "content": "You are a marketing advisor for Coca Cola. Your job is to create the text in Spanish for a new promotion poster in a " + content1 + "."},
      {"role": "user", "content": "Use the following products: " + content2 + '''. Limit to 10 words. Limit the text to 15 characters per line. The text should be in Spanish. Choose a setting background for the ad poster (max 5 words). Finally, choose a position for the text (top-left, top-center, top-right, middle-left, middle-right).
      
      Output format:
      
          Text: Text for the ad poster, use \n to separate lines
          Background: The setting background for the ad poster, in English
          Position: The position for the text (top-left, top-center, top-right, middle-left, middle-right)
      
      '''},
      
  ]

  content1 = Entorno
  content2 = ", ".join(Products)

  promocion = [
      {"role": "system", "content": "You are a marketing advisor for Coca Cola. Your job is to create the text in Spanish for a new promotion poster in a " + content1 + ". Were one product being free if you buy the other two."},
      {"role": "user", "content": "Use the following products: " + content2 + '''. Limit to 15 words. Limit the text to 10 characters per line. The text should be in Spanish. Choose a setting background for the ad poster (max 5 words). Finally, choose a position for the text (top-left, top-center, top-right, middle-left, middle-right).
      
      Output format:
      
          Text: Text for the ad poster, use \n to separate lines
          Background: The setting background for the ad poster, in English
          Position: The position for the text (top-left, top-center, top-right, middle-left, middle-right)
      
      '''},
      
  ]

  response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=promocion,
      temperature = 0.5,
      max_tokens = 200
      )

  responses.append(response)
  n += 1


  text = responses[-1]["choices"][0]["message"]["content"]

  # Save the results in three different variables
  m = re.match(r'(Text:\s\n)(?P<texto>[\w\S\s]*)(\n\nBackground:\s)(?P<fondo>[\w\S\s]*)(\n\nPosition:\s)(?P<posicion>[\w\S\s]*)', text)
  m.groupdict()

  texto = m.group('texto')
  fondo = m.group('fondo')
  posicion = m.group('posicion')

  # return {'text':texto, 'background':fondo, 'position':posicion}
  return [texto, fondo, posicion]

def image_generation(prompt, save_as, img_type):
  model_id = "stabilityai/stable-diffusion-2-1"

  # Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
  pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
  pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
  pipe = pipe.to("cuda")

  image = pipe(prompt).images[0]
  
  image.save(save_as, img_type)


def retrieve_image(producto, path):
    # Obtener la lista de carpetas disponibles
    carpetas = [carpeta for carpeta in os.listdir(path) if os.path.isdir(os.path.join(path, carpeta))]

    # Verificar si la carpeta existe
    for carpeta in carpetas:
        if producto.lower() in carpeta.lower():
            ruta_carpeta = os.path.join(path, carpeta)
            # Obtener la lista de archivos en la carpeta
            archivos = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.endswith(".png")]

            # Seleccionar una imagen aleatoria
            if archivos:
                imagen_seleccionada = random.choice(archivos)

                # Mostrar la ruta completa de la imagen seleccionada
                ruta_imagen = os.path.join(ruta_carpeta, imagen_seleccionada)

                # Guardar la imagen seleccionada con un nombre temporal
                ruta_temporal = path + "/temp.png"
                Image.open(ruta_imagen).save(ruta_temporal)
                break
            else:
                print(f"No hay imágenes para {producto}.")
                break
    else:
        print(f"No existe la carpeta para {producto}.")

    return ruta_temporal if archivos else None



def draw_text_on_image(text, size, font_type, position_par, background_img, font_color = 'white'):

    # Open the background image
    img = Image.open(background_img)

    # Create a draw object
    draw = ImageDraw.Draw(img)

    # Calculate text width based on the size parameter
    text_width = int(img.width * size) * 2

    # Set font size based on text width
    font_size = int(text_width / max([len(x) for x in text.split('\n')])) # int(text_width / len(text))  # Adjust based on the length of the text
    font = ImageFont.truetype(font_type, font_size)

    # Get the size of the text
    text_size = draw.textbbox((0,0), text, font=font)

    # Stablishing positions based on image and text size
    positions = {'center':(int(img.width / 2 - text_size[0] / 2), int(img.height / 2 - text_size[1] / 2)),
                 'top-left':(int(img.width * 0.05), int(img.height * 0.05)),
                 'top-right':(int(img.width * 0.95 - text_size[0]), int(img.height * 0.05)),
                 'top-center':(int(img.width / 2 - text_size[0] / 2), int(img.height * 0.05)),
                 'middle-left':(int(img.width * 0.05), int(img.height / 2 - text_size[1] / 2)),
                 'middle-right':(int(img.width * 0.95 - text_size[0]), int(img.height / 2 - text_size[1] / 2))}

    # Draw the text
    draw.text(positions[position_par], text, font=font, fill=font_color)  # You can change 'white' to the desired text color
    
    # Disclaimer
    disclaimer = "HIDRÁTATE DIRARIAMENTE. Consulta términos y condiciones:\nEsta imagen es una prueba de concepto para Arca Continental."
    font_mini = ImageFont.truetype(font_type, 15)
    draw.text((25, img.width-70), disclaimer, font=font_mini, fill=font_color)

    # Return the modified image
    return img



def draw_products(img, products, text_position, scale_obj = 0.9):
  '''
  image_if_text = {'top-left':'bottom-right',
                  'top-right':'bottom-left',
                  'top-center':'bottom-center',
                  'middle-left': 'middle-right',
                  'middle-right':'middle-left'}
  '''
  init_position = {'bottom-right':(scale_obj, scale_obj),
                  'bottom-left':(-0,1, scale_obj),
                  'bottom-center':(0.5, 0.7),
                  'middle-right':(scale_obj, scale_obj/2),
                  'middle-left':(-0.1, scale_obj/2)}

  loc_obj = init_position['bottom-center'] # init_position[image_if_text[text_position]]


  obj = Image.open('products/image0.png')
  # display(obj)
  # Scale image to the desired size
  scaled_size = (int(obj.size[0] * scale_obj), int((obj.size[1] * int(obj.size[0] * scale_obj)) / obj.size[0]))
  obj = obj.resize(scaled_size)

  loc_obj_adj = (int(loc_obj[0] * (img.size[0] - scaled_size[0])), int(loc_obj[1] * (img.size[1] - scaled_size[1])))
  img.paste(obj, loc_obj_adj, mask = obj)

#  loc_obj = (loc_obj[0] + obj.size[0]/1000, loc_obj[1])

  # Logo
  obj = Image.open('logo.png')
  scaled_size = (int(obj.size[0] * 0.3), int((obj.size[1] * int(obj.size[0] * 0.3)) / obj.size[0]))
  logo = obj.resize(scaled_size)
  img.paste(logo, (img.width-logo.width-30, img.height-logo.height - 30), mask = logo)

  return img



# --------------------------------------------------------------------------------------------------


def main(environment, products):
  text, background, text_position = text_generation(environment, products)
  background = background + ' with a ' + products[1] + ' in only dark colors'
  text_position = 'top-left'
  
  # Generation of Background
  image_generation(background, 'background_image.jpg', 'JPEG')

  # Product Images Retrieval
  for i in range(len(products)):
    product_name = products[i]
    ruta_imagen = retrieve_image(product_name, os.path.join(os.getcwd(), "ImagenesPublicidad"))
    # ruta_imagen = retrieve_image(product_name, "/content/gdrive/MyDrive/Imagenes_Publicidad_Reto")

    if ruta_imagen:
        imagen = Image.open(ruta_imagen)
        imagen.save('products/image' + str(i) + '.png', 'PNG')

    else:
        print("No image found.")



  # Image
  background_img = Image.open('background_image.jpg')
  background_img = background_img.filter(ImageFilter.BLUR)
  # Drawing Products
  result_img = draw_products(background_img, products, text_position) #result_img
  result_img.save("new_background_image.jpg", 'JPEG')
  # Text
  flyer = draw_text_on_image(text, 0.7, "OpenSans-Bold.ttf", text_position, "new_background_image.jpg")

  # Final Image
  flyer.save('flyer.jpg', 'JPEG')


# --------------------------------------------------------------------------------------------------

'''
products =  ['Sprite 2L', 'Coca-Cola 355ml']
background = 'Beach with sunset with Coca-Cola 355ml'
text = '¡Llévate un Sprite\ncon una Coca-Cola 2L'
text_position = 'top-left'

background = m.group('fondo')
text = m.group('texto')
text_position = m.group('posicion')
'''
main('Tienda', ['Sprite 2L', 'Coca-Cola 355ml'])
