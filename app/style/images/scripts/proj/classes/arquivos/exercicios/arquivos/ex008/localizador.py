def buscar_palavra(palavra_alvo:str):
    with open('documento.txt', 'r') as arquivo:
        encontrou = False 
        linhas = arquivo.readlines() 

    # Função que numera automaticamente cada item de um arquivo ou lista enquanto um loop é aplicado.
        for indice, linha in enumerate(linhas, start=1):
            if palavra_alvo in linha:
                print(f'Linha [{indice}]: {linha.strip()}')
                encontrou = True
    
        if not encontrou:
            print('A palavra não encontra-se no texto.')

if __name__ == '__main__':
    buscar_palavra("facilita")