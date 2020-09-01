def doblar_valor(numero):
    numero*=2
n=10
doblar_valor(n)
print(n)#Pasamos solo valor, no se afecta, es una copia

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valores(ns)
print(ns)#se afecta directamente la variable