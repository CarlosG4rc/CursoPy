numeros = [1,2,3,4]
datos = [4, "una cadena",-15,3.14,"Otra cadena"]

print(datos[0])
print(datos[1])
print(datos[-2:])

print(numeros + [5,6,7,8])

pares = [0,2,4,5,8,10]
print("pares incorrectos" )
print(pares)
pares[3]=6 #modificar valores
print("pares correctos")
print(pares)
pares.append(12) #agregar valores
print(pares)

letras=['a','b','c','d','e','f']
print(letras[:3])
letras[:3]=['x','y','z']#modificamos datos con slicing
print(letras)

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
r=[a,b,c]
print(r)
print(r[0])
print(r[2][0])