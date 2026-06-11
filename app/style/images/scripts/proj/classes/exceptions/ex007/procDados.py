def processar_dados(lista:list, indice:int):
    if indice >= len(lista):
        raise IndexError('O indice não existe.')
    
    if not isinstance(lista[indice], int):
        raise TypeError('Tipo não suportado para operação matematica')
    
    else:
        resultado = lista[indice] / 2 
    
    
if __name__ == '__main__':
    try:
        processar_dados({1,2,3,4,5}, 10)  
    except IndexError:
        ('Indice invalido')
    


    