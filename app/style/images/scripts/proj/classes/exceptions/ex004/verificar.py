def verificar_numero(self, numero:int):
    if numero < 0:
        raise ValueError('O numero não pode ser negativo')
    
    