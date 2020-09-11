class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este metodo lo heredo de A")
class B:
    def __init__(self):
        print("soy de clase B")
    def b(self):
            print("Este metodo lo heredo de B")

class C(B,A):
    def c(self):
            print("Este metodo lo heredo de C")

c = C()#dá prioridad a B se sobre-escribe
c.a()
c.b()
c.c()