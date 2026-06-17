def buscar_palavra(palavra_alvo:str):
    with open('documento.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
