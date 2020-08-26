pila = [3,4,5]# Listas Lifo
pila.append(6)
pila.append(7)

print(pila)
n=pila.pop()
print(n) #print(pila.pop) es lo mismo ~
print(pila)

from collections import deque #Para usar colas hay que ocupar librerias
cola = deque()
cola = deque(['Hector','Juan','Miguel'])
print(cola)

cola.append('Maria')
cola.append('Armando')

print(cola)

print(cola.popleft())
print(cola)