class Pelicula:
    #Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película" ,self.titulo)

    #Destructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula", self.titulo)

    #Redefinimos el método string
    def __str__(self):
        return("{} lanzada {} con una duracion de {} minutos".format(self.titulo,self.lanzamiento,self.duracion))

    #redefinimos metodo len
    def __len__(self):
        return self.duracion

p = Pelicula("El padrino",175,1972)
print(str(p))
print("La pelicula dura ", len(p))