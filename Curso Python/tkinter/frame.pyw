from tkinter import *

root = Tk()

root.title("Hola mundo")
root.resizable(1,1) #vertical,horizontal
root.iconbitmap('hola.ico')

frame = Frame(root, width = 480, height = 320)
#frame.pack(side = "bottom", anchor = "w")
frame.pack(fill = 'both', expand = 1)
frame.config(cursor = "pirate")
frame.config(bg = "lightblue")
frame.config(bd = 25)
frame.config(relief = "sunken")



root.config(cursor = "arrow")
root.config(bg = "blue")
root.config(bd = 15)
root.config(relief = "ridge")


root.mainloop()#abajo del todo