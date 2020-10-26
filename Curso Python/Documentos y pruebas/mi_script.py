
def suma(a,b):
    """La funcion suma(a,b) recibe dos parametros a y b.
    Devuelve la suma de ambos
    
    >>> suma(5,10)
    15

    """
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

help(suma)