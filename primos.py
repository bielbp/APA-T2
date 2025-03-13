"""
Biel Bernal Pratdesaba
""" 

def esPrimo(numero,):
    """
    Devuelve true si el numero es primo y false si no lo es.
    """
    for prueva in range(2, numero):
        if numero % prueva == 0:
            return False
    return True



    