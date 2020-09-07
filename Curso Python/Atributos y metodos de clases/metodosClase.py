class Galleta():
    chocolate = False
    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color 
        print("Se acaba de crear una galleta {} y {}.".format(sabor,color))

    def chocolatear(self):
        self.chocolate = True #self hace referencia a sí mismo

    def tiene_chocolate(self):
        if(self.chocolate):
            print("Soy una calleta chocolateada :P")
        else:
            print("Soy una galleta sin chocolate :(")

g = Galleta("salada", "marrón")
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()