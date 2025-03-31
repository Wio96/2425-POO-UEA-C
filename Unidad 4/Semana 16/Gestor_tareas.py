import tkinter as tk
from tkinter import messagebox

# Funciones para las acciones de la aplicación
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)  # Limpiar campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

def marcar_completada():
    try:
        seleccion = lista_tareas.curselection()
        tarea_seleccionada = lista_tareas.get(seleccion)
        tarea_completada = tarea_seleccionada + " (Completada)"
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion, tarea_completada)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

def cerrar_aplicacion(event):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear un Frame para organizar los widgets
frame = tk.Frame(root)
frame.pack(pady=20)

# Crear un campo de entrada para agregar nuevas tareas
entrada_tarea = tk.Entry(frame, width=40)
entrada_tarea.pack(padx=10, pady=10)

# Crear botones para añadir, marcar como completada y eliminar tareas
btn_agregar = tk.Button(frame, text="Agregar Tarea", width=20, command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(frame, text="Marcar como Completada", width=20, command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(frame, text="Eliminar Tarea", width=20, command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Crear una lista para mostrar las tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(pady=10)

# Vincular atajos de teclado
root.bind("<Return>", lambda event: agregar_tarea())  # Tecla Enter para agregar tarea
root.bind("<C>", lambda event: marcar_completada())  # Tecla C para marcar como completada
root.bind("<Delete>", lambda event: eliminar_tarea())  # Tecla Delete para eliminar tarea
root.bind("<D>", lambda event: eliminar_tarea())  # Tecla D para eliminar tarea
root.bind("<Escape>", cerrar_aplicacion)  # Tecla Escape para cerrar la aplicación

# Ejecutar el bucle principal
root.mainloop()
