"""
Biel Bernal Pratdesaba

>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
""" 

# Determinación de la primalidad y descomposición de un número en factores primos
from collections import Counter

def esPrimo(numero):
    """
    Devuelve true si el numero es primo y false si no lo es.
    """
    if numero < 2:
        return False
    for prueva in range(2, int(numero ** 0.5) + 1):
        if numero % prueva == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.
    """
    llista = []
    for prova in range(2, numero):
        if esPrimo(prova):
            llista.append(prova)
    return tuple(llista) 

def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento.
    """
    factors = []
    for primo in primos(numero + 1):
        while numero % primo == 0:
            factors.append(primo)
            numero = numero // primo
        if numero == 1:
            break
    return tuple(factors)

# Obtención del mínimo común múltiplo y el máximo común divisor
def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
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
    """
    tupla1 = Counter(descompon(numero1))
    tupla2 = Counter(descompon(numero2))
    comuns = tupla1 & tupla2

    maximcomu = 1
    for factor in comuns:
        maximcomu *= factor ** comuns[factor]
    return maximcomu

# Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos
def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    resultat = numeros[0]
    for numero in numeros[1:]:
        resultat = mcm(resultat, numero)
    return resultat
        
def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    resultat = numeros[0]
    for numero in numeros[1:]:
        resultat = mcd(resultat, numero)
    return resultat

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)