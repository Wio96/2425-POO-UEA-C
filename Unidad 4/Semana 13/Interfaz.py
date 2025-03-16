import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar():
    texto = entrada.get()
    if texto:
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)  # Borra el campo de texto después de agregar
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño de la ventana

# Etiqueta
tk.Label(ventana, text="Ingrese un dato:").pack(pady=5)

# Campo de entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=5)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
