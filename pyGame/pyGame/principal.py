from tkinter import *
import main

main = Main()
def boton():
    print("HOLA")

ventana = Tk()
ventana.geometry("650x490+0+0")
btmDibujar = Button(ventana, text="Ingresar camino", font = ("Agency FB", 14), command=boton).place(x=280, y=245)

ventana.mainloop()