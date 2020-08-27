v = "otro texto"
n = 10

print("Un texto" , v , "y un numero " , n)
c = "un texto '{}' y un número '{}'".format(v,n)
print(c)
print("Un texto '{0}' y un número '{1}'".format(v,n))
print("Un texto '{1}' y un número '{0}'".format(v,n))
print("Un texto '{texto}' y un número '{numero}'".format(texto=v,numero=n))

print("{v},{v},{v}".format(v=v))

print( "{:>30}".format("palabra") )
print( "{:30}".format("palabra") )
print( "{:^30}".format("palabra"))
print( "{:.3}".format("palabra"))
print( "{:>30.3}".format("palabra") )

#formateo de numeros enteros, rellenos con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

#formateo de numeros enteros, rellenos con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#formateo de numeros flotantes, rellenos con espacios

print("{}".format(3.1415926))
print("{:07.4f}".format(3.1415926))
print("{:07.4f}".format(153.21))