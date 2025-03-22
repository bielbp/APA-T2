"""
Biel Bernal Pratdesaba

>>> esPrimo(5)
True

>>> esPrimo(2)
True

>>> esPrimo(74211)
False

""" 

def esPrimo(numero,):
    """
    Devuelve true si el numero es primo y false si no lo es.

    >>> for numero in range(2, 10): 
    ...     print(esPrimo(numero))
    True
    True
    False
    True
    False
    True
    False
    False
    """
    for prueva in range(2, numero):
        if numero % prueva == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()


def primos(numero,):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.
    """
    llista = []
    for prova in range(2, numero):
        if esPrimo(prova) == True:
            llista.append(prova)
    return tuple(llista) 


def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento.
    """
    factors = []
    for primo in primos(numero):
        while numero % primo == 0:
            factors.append(primo)
            numero = numero // primo
        if numero ==1:
            break
    return tuple(factors)



