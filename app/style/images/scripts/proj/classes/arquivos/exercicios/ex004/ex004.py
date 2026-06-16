def contar_linhas_arquivo(nome_arquivo:str):
    arquivo = open(nome_arquivo, 'r')
    with open(nome_arquivo, 'r') as archive:
        for line in archive.readlines():
            if line.endswith('\n') or line.startswith('\n'):
                count+=1
            contagem = count
            print(contagem)

    if __name__ == '__main__':
        contar_linhas_arquivo('Fazendinha.txt')
    

