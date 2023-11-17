"""Modulo que contiene la interfaz gráfica de usuario para la selección de entorno y productos."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
from flyer_generation_oneproduct import main
# Asegúrate de que esta línea corresponda al nombre de tu script y función

# Carga los datos necesarios para la UI
df = pd.read_csv("promotion.csv", encoding="ISO-8859-1")
env_rules_df = pd.read_csv("env_rules.csv", encoding="latin")
entornos = env_rules_df["Entorno"].tolist()

def actualizar_seleccion():
    """Función que se ejecuta al presionar el botón "Confirmar selección"."""
    entorno = entorno_var.get()
    selected_indices = listbox_productos.curselection()
    products = [listbox_productos.get(idx) for idx in selected_indices]

    if not products:
        print("¡Debes seleccionar al menos un producto!")
        return

    # Aquí puedes llamar a la función main con los parámetros obtenidos
    main(entorno, products)

    # Cargar y mostrar la imagen resultante
    try:
        flyer_image = Image.open('flyer.jpg')
        flyer_photo = ImageTk.PhotoImage(flyer_image)

        flyer_label = tk.Label(root, image=flyer_photo)
        flyer_label.image = flyer_photo  # Mantener una referencia
        flyer_label.pack()  # Ajustar la posición según sea necesario
    except IOError:
        print("Error al cargar la imagen resultante.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Selección de Entorno y Productos")
root.geometry("1000x1000")

# Cargar y configurar la imagen de fondo
background_image = Image.open('Bckgd.png')
background_image = background_image.resize((1000, 1000), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Estilos para mejorar la apariencia
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")

# Menú desplegable para seleccionar el entorno
label_entorno = ttk.Label(root, text="Selecciona el entorno:", background="#ffffff")
label_entorno.pack(pady=5)

entorno_var = tk.StringVar()
entorno_menu = ttk.Combobox(root, textvariable=entorno_var, values=entornos)
entorno_menu.pack(pady=5)

# Lista de productos seleccionables
label_productos = ttk.Label(root, text="Selecciona los productos:", background="#ffffff")
label_productos.pack(pady=5)

productos_unicos = set(df['Producto'])
listbox_productos = tk.Listbox(root, selectmode=tk.MULTIPLE,
                               exportselection=0, selectbackground="#a6a6a6")
for producto in productos_unicos:
    listbox_productos.insert(tk.END, producto)
listbox_productos.pack(pady=5)

# Botón para confirmar selección
boton_confirmar = ttk.Button(root, text="Confirmar selección", command=actualizar_seleccion)
boton_confirmar.pack(pady=10)

root.mainloop()
