def processar_dados(lista:list, indice:int):
    if indice >= len(lista):
        raise IndexError('O indice não existe.')
    
    if not isinstance(lista[indice], int):
        raise TypeError('Tipo não suportado para operação matematica')
    
    else:
        return lista[indice] / 2 
    
    
if __name__ == '__main__':
    try:
        processar_dados([1,3,2,0,-1], 8)
        processar_dados([1,3,'a',0,-1], 2)
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)
    


    