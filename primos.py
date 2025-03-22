"""
Biel Bernal Pratdesaba

>>> esPrimo(5)
True

>>> esPrimo(2)
True

>>> esPrimo(74211)
False

""" 
# Determinación de la *primalidad* y descomposición de un número en factores primos

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

def primos(numero,):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.

    >>> for numero in range(2,10):
    ...     print(primos(numero))
    ()
    (2,)
    (2, 3)
    (2, 3)
    (2, 3, 5)
    (2, 3, 5)
    (2, 3, 5, 7)
    (2, 3, 5, 7)
    """
    llista = []
    for prova in range(2, numero):
        if esPrimo(prova) == True:
            llista.append(prova)
    return tuple(llista) 

def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento.

    >>> for numero in [6, 60, 13, 1, 100]:
    ...     print(descompon(numero))
    (2, 3)
    (2, 2, 3, 5)
    ()
    ()
    (2, 2, 5, 5)
    """
    factors = []
    for primo in primos(numero):
        while numero % primo == 0:
            factors.append(primo)
            numero = numero // primo
        if numero ==1:
            break
    return tuple(factors)

# Obtención del mínimo común múltiplo y el máximo común divisor

from collections import Counter

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcm(60, 48)
    240
    >>> mcm(100, 80)
    400
    """
    tupla1 = Counter(descompon(numero1))
    tupla2 = Counter(descompon(numero2))
    comuns = tupla1 | tupla2

    minimcomu = 1
    for num in comuns:
        minimcomu *= num ** comuns[num]
    return minimcomu


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de dos números usando la descomposición en factores primos.

    >>> mcd(60, 48)
    12
    >>> mcd(100, 80)
    20
    """
    tupla1 = Counter(descompon(numero1))
    tupla2 = Counter(descompon(numero2))
    comuns = tupla1 & tupla2

    maximcomu = 1
    for factor in comuns:
        maximcomu *= factor ** comuns[factor]
    return maximcomu

if __name__ == "__main__":
    import doctest
    doctest.testmod()
