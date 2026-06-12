from numeronegativoError import NumeronegativoError

def calcular_raizQuadrada(numero: int):
    if numero < 0:
        raise NumeronegativoError
    
    if not isinstance(numero, (int, float)):
        raise TypeError('Calculo indisponivel para operador especifico.')
