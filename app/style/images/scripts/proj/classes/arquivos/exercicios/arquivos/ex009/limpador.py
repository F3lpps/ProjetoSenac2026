def limpar_arquivo(origem: str, destino: str):
    with open(origem, 'r') as arquivo_origem:
        counteudo = arquivo_origem.readlines()
        
        counteudo_limpo = [linha.strip() for linha in counteudo if linha.strip()]

    with open(destino, 'w') as arquivo_destino:
        arquivo_destino.write('\n'.join(counteudo_limpo) + '\n')

if __name__ == '__main__':
    limpar_arquivo("dados_sujos.txt", "dados_limpos.txt")





        






    

    