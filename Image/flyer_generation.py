'''
Previous set-tup

! pip install diffusers transformers accelerate scipy safetensors
! mkdir products

'''

import os
import random


# For background image generation
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# For image manipulation
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw,ImageFont


from google.colab import drive
drive.mount("/content/gdrive")


# --------------------------------------------------------------------------------------------------------------------

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
    text_size = draw.textsize(text, font=font)

    # Stablishing positions based on image and text size
    positions = {'center':(int(img.width / 2 - text_size[0] / 2), int(img.height / 2 - text_size[1] / 2)),
                 'top-left':(int(img.width * 0.05), int(img.height * 0.05)),
                 'top-right':(int(img.width * 0.95 - text_size[0]), int(img.height * 0.05)),
                 'top-center':(int(img.width / 2 - text_size[0] / 2), int(img.height * 0.05)),
                 'middle-left':(int(img.width * 0.05), int(img.height / 2 - text_size[1] / 2)),
                 'middle-right':(int(img.width * 0.95 - text_size[0]), int(img.height / 2 - text_size[1] / 2))}

    # Draw the text
    draw.text(positions[position_par], text, font=font, fill=font_color)  # You can change 'white' to the desired text color

    # Return the modified image
    return img



def draw_products(img, text_position, scale_obj = 0.9):
  image_if_text = {'top-left':'bottom-right',
                  'top-right':'bottom-left',
                  'top-center':'bottom-center',
                  'middle-left': 'middle-right',
                  'middle-right':'middle-left'}



  init_position = {'bottom-right':(scale_obj, scale_obj),
                  'bottom-left':(-0,1, scale_obj),
                  'bottom-center':(0.4, scale_obj),
                  'middle-right':(scale_obj, scale_obj/2),
                  'middle-left':(-0.1, scale_obj/2)}

  loc_obj = init_position[image_if_text[text_position]]

  for i in range(len(products)):
    # print(i)
    obj = Image.open('products/image' + str(i) + '.png')
    # display(obj)
    # Scale image to the desired size
    scaled_size = (int(obj.size[0] * scale_obj), int((obj.size[1] * int(obj.size[0] * scale_obj)) / obj.size[0]))
    obj = obj.resize(scaled_size)

    loc_obj_adj = (int(loc_obj[0] * (img.size[0] - scaled_size[0])), int(loc_obj[1] * (img.size[1] - scaled_size[1])))
    img.paste(obj, loc_obj_adj, mask = obj)


    loc_obj = (loc_obj[0] + obj.size[0]/1000, loc_obj[1])

  return img



# -------------------------------------------------------------------------------------------------------------------


def main(products, background, text, text_position):
  # Generation of Background
  image_generation(background, 'background_image.jpg', 'JPEG')

  # Product Images Retrieval
  for i in range(len(products)):
    product_name = products[i]
    ruta_imagen = retrieve_image(product_name, "/content/gdrive/MyDrive/Imagenes_Publicidad_Reto")

    if ruta_imagen:
        imagen = Image.open(ruta_imagen)
        imagen.save('products/image' + str(i) + '.png', 'PNG')

    else:
        print("No image found.")

  # Drawing Text
  background_img = Image.open('background_image.jpg')
  result_img = draw_text_on_image(text, 0.5, "OpenSans-Bold.ttf", text_position, "background_image.jpg")

  # Drawing Products
  flyer = draw_products(result_img, text_position)

  # Final Image
  flyer.save('flyer.jpg', 'JPEG')


# -------------------------------------------------------------------------------------------------------------------


products =  ['Sprite 2L', 'Coca-Cola 355ml']
background = 'Beach with sunset'
text = '¡El doble de bebidas\nal precio de una!\nLlevate un Sprite\ncon una Coca-Cola 2L'
text_position = 'middle-left'
'''
background = m.group('fondo')
text = m.group('texto')
text_position = m.group('posicion')
'''
main(products, background, text, text_position)