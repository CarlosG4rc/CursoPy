class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia=referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    def __str__(self):
        return '''\
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}''' .format(self.referencia, self.nombre, self.pvp, self.descripcion)
class Adorno(Producto): #es hija de clase Producto
    pass
class Alimento(Producto): #hija de clase Producto
    def __str__(self):
        return '''
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}''' .format(self.referencia, self.nombre, self.pvp, self.descripcion,self.productor,self.distribuidor)
    productor = ""
    distribuidor = ""
class Libro(Producto): #hija de clase Producto
    isbn = ""
    autor = ""
    def __str__(self):
        return '''
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}
        ISBN\t\t{}
        AUTOR\t\t{}''' .format(self.referencia, self.nombre, self.pvp, self.descripcion,self.isbn,self.autor)
    productor = ""
    distribuidor = ""

a = Adorno(2034,"Vaso adornado", 15, "Vaso de porcelana adornado con árboles")
al = Alimento(2035, "Botella de Aceite de Oliva Extra", 5,"250 ml")
al.productor = "La aceitera"
al.distribuidor = "Distribuciones SA"
l = Libro(2036, "Quijote de la mancha", 16, "Libro del Quijote de la Mancha")
l.isbn = "0-1234-78-9"
l.autor ="Miguel de Servantes"
print(a)
print(al)
print(l)

productos = [a, al]

productos.append(l)
for p in productos:
    if(isinstance(p,Adorno)):
        print (p.referencia,p.nombre)
    elif(isinstance(p,Alimento)):
        print (p.referencia,p.productor)
    elif(isinstance(p, Libro)):
        print (p.referencia, p.nombre, p.isbn)
def rebajar_producto(p,rebaja):
    p.pvp = p.pvp -(p.pvp/100 * rebaja)
    return p
al_rebajado = rebajar_producto(al,10)
print(al_rebajado)
print(al)#Se ha modificado al tambien
