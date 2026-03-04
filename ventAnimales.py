import tkinter as tk
from PIL import Image, ImageTk

def ventana_principal():
    global ven1, var
    ven1 = tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("600x300")
    ven1.config(bg="blue")

    eti1 = tk.Label(ven1, text="Reino Animal", bg="lightblue", font=("Arial", 23, "bold"))
    eti1.pack()

    frame1 = tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=10, pady=10)

    # Cargar imagen principal
    imagen = Image.open("C:/Users/Salon202/Desktop/berna/reinoanimal.jpg")
    imagen = imagen.resize((400, 200)) # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.image = imagen_tk # Mantener referencia
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    frame2 = tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)

    var = tk.IntVar()

    ele = tk.Radiobutton(frame2, text="Elefante", variable=var, value=1)
    ele.pack()
    jirafa = tk.Radiobutton(frame2, text="Jirafa", variable=var, value=2)
    jirafa.pack()
    capibara = tk.Radiobutton(frame2, text="Capibara", variable=var, value=3)
    capibara.pack()
    leon = tk.Radiobutton(frame2, text="León", variable=var, value=4)
    leon.pack()

    def informacion():
        seleccion = var.get()
        if seleccion == 1:    
            ventana_elefante()
        elif seleccion == 2:
            ventana_jirafa()
        elif seleccion == 3:
            ventana_capibara()
        elif seleccion == 4:
            ventana_leon()

    boton1 = tk.Button(ven1, text="Ver info", command=informacion)
    boton1.pack()

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() # Cerrar la segunda ventana
    ventana_principal() # Volver a abrir la ventana principal

def ventana_elefante():
    global ven2
    ven1.destroy()
    ven2 = tk.Tk()
    ven2.title("Información del elefante")
    ven2.geometry("700x500")
    ven2.config(bg="gray")

    eti2 = tk.Label(ven2, text="Elefante", bg="gray", font=("Algerian", 24, "bold"))
    eti2.pack(pady=10)

    frame3 = tk.Frame(ven2)
    frame3.pack(pady=20)

    # Cargar imagen del elefante
    imagen2 = Image.open("C:/Users/Salon202/Desktop/berna/reinoanimal.jpg")
    imagen2 = imagen2.resize((400, 200)) # Redimensionar si es necesario
    imagen_tk2 = ImageTk.PhotoImage(imagen2)
    label_imagen = tk.Label(frame3, image=imagen_tk2)
    label_imagen.image = imagen_tk2 # Mantener referencia
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    texto_info = ("La jirafa es una especie de mamífero artiodáctilo, de la familia Giraffidae propio de África." \
    " Es la más alta de todas las especies de animales terrestres existentes, ya que puede alcanzar una altura máxima de 5,7m y un peso que varía entre 750 y 1600kg.")
    
    etiqueta2 = tk.Label(frame3, text=texto_info, wraplength=200, justify="left")
    etiqueta2.grid(row=0, column=1, padx=5, pady=5)

    boton2 = tk.Button(ven2, text="ir a ventana principal", command=lambda: regresar_a_primera(ven2))
    boton2.pack(pady=30)

def ventana_jirafa():
    global ven3
    ven1.destroy()
    ven3 = tk.Tk()
    ven3.title("Información del jirafa")
    ven3.geometry("700x500")
    ven3.config(bg="gray")

    eti = tk.Label(ven3, text="Jirafa", bg="gray", font=("Algerian", 24, "bold"))
    eti.pack(pady=10)

    frame4 = tk.Frame(ven3)
    frame4.pack(pady=20)

    # Cargar imagen de la jirafa
    imagen3 = Image.open("C:/Users/Salon202/Desktop/berna/jirafa.jpg")
    imagen3 = imagen3.resize((400, 200)) # Redimensionar si es necesario
    imagen_tk2 = ImageTk.PhotoImage(imagen3)
    label_imagen = tk.Label(frame4, image=imagen_tk2)
    label_imagen.image = imagen_tk2 # Mantener referencia
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    texto_info = ("La jirafa es una especie de mamífero artiodáctilo, de la familia Giraffidae propio de África. Es la más alta de todas las especies de animales terrestres existentes, ya que puede alcanzar una altura máxima de 5,7 m y un peso que varía entre 750 y 1600 kg.")
    
    etiqueta = tk.Label(frame4, text=texto_info, wraplength=200, justify="left")
    etiqueta.grid(row=0, column=1, padx=5, pady=5)

    boton = tk.Button(ven3, text="ir a ventana principal", command=lambda: regresar_a_primera(ven3))
    boton.pack(pady=30)

    ven3.mainloop()

def ventana_capibara():
    global ven4
    ven1.destroy()
    ven4 = tk.Tk()
    ven4.title("Información del Capibara")
    ven4.geometry("700x500")
    ven4.config(bg="brown")

    eti = tk.Label(ven4, text="Capibara", bg="gray", font=("Algerian", 24, "bold"))
    eti.pack(pady=10)

    frame5 = tk.Frame(ven4)
    frame5.pack(pady=20)

    # Cargar imagen del capibara
    imagen3 = Image.open("C:/Users/Salon202/Desktop/berna/capibara.jpg")
    imagen3 = imagen3.resize((400, 200)) # Redimensionar si es necesario
    imagen_tk2 = ImageTk.PhotoImage(imagen3)
    label_imagen = tk.Label(frame5, image=imagen_tk2)
    label_imagen.image = imagen_tk2 # Mantener referencia
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    texto_info = ("El capibara, carpincho, chigüire o ronsoco, entre otras denominaciones, es una especie de roedor caviomorfo de la familia de los cávidos, nativa de Sudamérica. Se trata del roedor viviente de mayor tamaño y peso del mundo.​El otro miembro existente de ese género es el capibara menor.")
    
    etiqueta = tk.Label(frame5, text=texto_info, wraplength=200, justify="left")
    etiqueta.grid(row=0, column=1, padx=5, pady=5)

    boton = tk.Button(ven4, text="ir a ventana principal", command=lambda: regresar_a_primera(ven4))
    boton.pack(pady=30)

    ven4.mainloop()

def ventana_leon():
    global ven5
    ven1.destroy()
    ven5 = tk.Tk()
    ven5.title("Información del Leon")
    ven5.geometry("700x500")
    ven5.config(bg="yellow")

    eti = tk.Label(ven5, text="Capibara", bg="gray", font=("Algerian", 24, "bold"))
    eti.pack(pady=10)

    frame6 = tk.Frame(ven5)
    frame6.pack(pady=20)

    # Cargar imagen del capibara
    imagen3 = Image.open("C:/Users/Salon202/Desktop/berna/leon.avif")
    imagen3 = imagen3.resize((400, 200)) # Redimensionar si es necesario
    imagen_tk2 = ImageTk.PhotoImage(imagen3)
    label_imagen = tk.Label(frame6, image=imagen_tk2)
    label_imagen.image = imagen_tk2 # Mantener referencia
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    texto_info = ("El león es un mamífero carnívoro de la familia de los félidos y una de las cinco especies del género Panthera.")
    
    etiqueta = tk.Label(frame6, text=texto_info, wraplength=200, justify="left")
    etiqueta.grid(row=0, column=1, padx=5, pady=5)

    boton = tk.Button(ven5, text="ir a ventana principal", command=lambda: regresar_a_primera(ven5))
    boton.pack(pady=30)

    ven4.mainloop()


# Iniciar el programa
ventana_principal()