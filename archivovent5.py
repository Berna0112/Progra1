import tkinter as tk
from tkinter import messagebox

def nuevo_archivo():
    messagebox.showinfo("informacion", "Craste un nuevo archivo")

def abrir_archivo():
    messagebox.showinfo("Informacion", "Abriste un archivo ") 

def guardar_archivo():
    messagebox.showinfo("Informacion", "Guardaste un archivo ")

def pegar_a():
    messagebox.showinfo("Informacion", "Pegaste un texto ")  
   
def cortar_a():
    messagebox.showinfo("Informacion", "Cortaste un texto ")    



ven1 = tk.Tk()
ven1.title("Esta es mi ventana principal")
ven1.geometry("600x600")
ven1.config(bg="grey")

barra_menu=tk.Menu(ven1)

menu_archivo=tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo archivo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)

menu_edicion=tk.Menu(barra_menu, tearoff=0)

menu_edicion.add_command(label="Cortar", command=cortar_a)
menu_edicion.add_command(label="Pegar", command=pegar_a)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edicion", menu=menu_edicion)
ven1.config(menu=barra_menu)

ven1.mainloop() 