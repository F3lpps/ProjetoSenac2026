def adiconar_notas(lista_notas:list, nova_nota:float):

    if 0 <= nova_nota <=10:
        lista_notas.append(nova_nota)
    print("Nota adicionada com sucesso!")
        
    if not isinstance(nova_nota, (int, float)):
        raise TypeError('Tipo de dado invalido.')
    
    else:
        raise ValueError('Valor abaixo')
    
if __name__ == "__main__":

    adiconar_notas({8,7,6,5}, 5.0)
