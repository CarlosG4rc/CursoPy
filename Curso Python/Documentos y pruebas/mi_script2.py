def palindromo(palabra):

    """
    La funcion palindromo(palabra) recibe una palabra.
    Si la palabra es un palindromo devuelve True, si no False

    Un palindromo es una palabra o frase que se lee igual
    tanto de izquierda a derecha como de derecha a izquierda
    """

    if palabra == palabra[::-1]:
        return True
    else:
        return False

# if __name__=="__main__":
#     import doctest
#     doctest.testmod()

print(palindromo("radat"))