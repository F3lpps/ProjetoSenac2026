def registrar_pontuacao(nome_jogador:str, pontos:int):
    arquivo = open('ranking.txt', 'a')
    with open('ranking.txt', 'r'):
        arquivo.write('Nome: {nome_jogador} - Pontos: {pontos}')

if __name__ == '__main__':

    registrar_pontuacao('Fulaninho', 10)
        
