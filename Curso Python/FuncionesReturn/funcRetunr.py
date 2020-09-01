def test():
    return "Una cadena Retornada"

c= test()
print(test())
print(c)

def cadena():
    return[1,2,3,4,5]


print(cadena())
print(cadena()[-1])

def several():
    return "una cadena",20,[1,2,3]

print(several()) #Tupla!!!!!
c,n,l = several()
print(c)
print(n)
print(l)