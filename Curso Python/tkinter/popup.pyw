from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

def test():
    # MessageBox.showinfo("Alerta", "seccion solo para administradores")
    # MessageBox.showwarning("Alerta", "seccion solo para administradores")
    #MessageBox.showerror("Alerta", "seccion solo para administradores")
    # resultado = MessageBox.askquestion("Salir", "¿Quieres Salir sin guardar")
    # if resultado == "yes":
    #     root.destroy()
    #resultado = MessageBox.askokcancel("Salir", "Sobre escribir el fichero actual?")
    # resultado = MessageBox.askyesno("Salir", "¿Quieres Salir sin guardar")
    # if resultado:
    #     root.destroy()

    resultado = MessageBox.askretrycancel("Reiniciar", "No se puede conectar")
    if resultado:
        root.destroy()


Button(root, text="Clicame", command=test).pack()




root.mainloop()#abajo del todo