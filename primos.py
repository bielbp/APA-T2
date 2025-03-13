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
