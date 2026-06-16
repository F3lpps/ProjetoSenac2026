def ler_poema():
    arquivo = open('poema.txt', 'r')
    with open('poema.txt', 'r') as arquivo:
        arquivo.read('poema.txt')
    print(arquivo.read)     
    if FileNotFoundError:
        raise  FileNotFoundError('Arquivo não encontrado :(')
    
if __name__ == '__main__':
    ler_poema()
    

    
    
