colores = {'amarillo':'yellow','azul':'blue','verde':'green'}
print(colores)
print(colores['azul'])

numeros = {10:'diez',20:'veinte'}
print(numeros[10])

colores['amarillo'] = 'white'
print(colores)

del(colores['amarillo'])
print(colores)

edades = {'Hector':27, 'Juan':45, 'Maria':34}
print(edades)
edades['Hector']+=1
print(edades)

for edad in edades: #no se accede a las edades si no a las palabras clave
    print(edad)
for clave in edades: #de esta manera si accedemos a los datos, por medio de la s claves
    print(edades[clave])
for clave in edades:
    print(clave,edades[clave])
for clave,valor in edades.items():
    print(clave,valor)
personajes = [] #lista

p = {'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Humano'}

personajes.append(p)

print(personajes)

p = {'Nombre':'Legolas', 'Clase':'Arquero', 'Raza':'Elfo'}

personajes.append(p)

p = {'Nombre':'Gimli', 'Clase':'Guerrero', 'Raza':'Enano'}

personajes.append(p)

print(personajes)

for p in personajes:
    print(p['Nombre'],p['Clase'],p['Raza'])