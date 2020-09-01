def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(5, "Hola",[1,2,3,4,5])

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," ",kwargs[kwarg])
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])
def super_funcion(*args,**kwargs):
    t=0
    for arg in args:
        t+=arg
    print("Sumatorio iterando es ", t) #Suma los argumentos por posición
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])#acomoda los argumentos por nombre

super_funcion(10,50,-1,1.56,nombre="Hector",edad=27)

