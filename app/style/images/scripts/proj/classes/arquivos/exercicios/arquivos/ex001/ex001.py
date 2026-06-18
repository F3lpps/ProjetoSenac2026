def gravar_diario(mensagem:str):
    arquivo = open('diario.txt', 'w')
    with open('diario.txt', 'a') as arquivo:
            arquivo.write(mensagem)

if __name__ == '__main__':
      gravar_diario('Sinto fome.')

