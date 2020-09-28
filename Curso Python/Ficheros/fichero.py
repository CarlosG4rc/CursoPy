from io import open
# texto = "Una linea con texto\nOtra linea con texto"
# fichero = open('fichero.txt','w')
# fichero.write(texto)
# fichero.close()
# fichero = open('fichero.txt','r')
# texto = fichero.read()
# fichero.close()
# print(texto)
# fichero = open('fichero.txt','r')
# lineas = fichero.readlines()
# fichero.close()
# print(lineas)
# fichero = open('fichero.txt','a')
# fichero.write('\nCuarta linea')
# fichero.close()
# fichero = open('fichero.txt','r')
# l = fichero.readline()
# print(l)
# l = fichero.readline()
# print(l)
# l = fichero.readline()
# print(l)
# l = fichero.readline()
# print(l)
# fichero.close()

# with open('fichero.txt', 'r') as fichero:
#     for linea in fichero:
#         print(linea)

# fichero = open('fichero.txt','r')
# fichero.seek(10)
# texto = fichero.read()
# print(texto)
# fichero.seek(0)
# fichero.read(5)
# texto = fichero.read()
# print(texto)
# fichero.close()

fichero = open('fichero.txt','r+')
lineas = fichero.readlines()
lineas[2] = "Esta linea ha sido modificada\n"
fichero.seek(0)
fichero.writelines(lineas)
print(lineas)

