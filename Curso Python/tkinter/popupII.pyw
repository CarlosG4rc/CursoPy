from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    # color = ColorChooser.askcolor(title="Elejir un color")
    # print(color)
    # ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:",
    #  filetypes=(("Fichero de texto", ".txt"),("Todos los ficheros", "*.*")))
 
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode = "a+", defaultextension=".txt") #a+ crea el fichero de cero Equivale a open('ruta', 'w')
    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()
    print(fichero)



Button(root, text="Clicame", command=test).pack()

root.mainloop()#abajo del todo