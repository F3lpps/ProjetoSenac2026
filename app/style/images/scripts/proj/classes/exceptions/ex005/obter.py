import traceback

def obter_elemento(lista:list, indice:int):
    if indice >= len(lista):
        raise IndexError('Posição inexistente')
        
    
    else:
        return lista(indice)
    
    
if __name__ == '__main__':
    try:
        obter_elemento([2, 4, 5, 6], 9)
    except IndexError as e:
        print("Erro capturado:", e)
        
