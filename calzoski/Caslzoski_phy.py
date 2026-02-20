import tkinter as tk
from PIL import Image, ImageTk
ven1=tk.Tk()
ven1.title("primera ventana")
ven1.geometry("1200x800")

etiqueta=tk.Label(ven1, text="Mi nombre es Bernardo", font=("Arial", 18, "bold"), fg="black", bg="purple", padx=20, pady=10)
etiqueta.pack()


etiqueta2=tk.Label(ven1, text="Estudio Ing: Ciencias de la Comp.", font=("Arial", 20, "bold"), padx=20, pady=10)
etiqueta2.pack()

etiqueta3=tk.Label(ven1, text="Mi comida favorita son las MILANESAS", font=("Arial", 30, "bold"), padx=20, pady=10)
etiqueta3.pack()

imagen=Image.open("calzoski.jpg")
imagen= imagen.resize((400,200))
imagen_tk= ImageTk.PhotoImage(imagen)
label_imagen= tk.Label(ven1, image=imagen_tk)
label_imagen.pack(pady=20)

def boton_clic():
    print("Hiciste click!")

boton=tk.Button(ven1, text="Haz click aqui", command=boton_clic,
                font=("Comic Sans", 30))
boton.pack(pady=20)

def actualizar_etiqueta():
    nuevo_texto=entrada.get()
    etiqueta4.config(text=nuevo_texto)
entrada= tk.Entry(ven1, width=60)
entrada.pack(pady=10)
boton2 = tk.Button(ven1, text="Actualizar", command=actualizar_etiqueta)
boton2.pack()

etiqueta4=tk.Label(ven1, text="Textp Inicial", font=("Arial, 12"))
etiqueta4.pack(pady=10)

ven1.mainloop()