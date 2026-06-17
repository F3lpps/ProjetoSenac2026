def somar_valores():
    arquivo = open('valores.txt', 'r')

    print("(12.5, 45.0, 7.2, 100.8, 23.1)")

    linhas = arquivo.readlines()
    arquivo.close

    soma = 0.0

    for linha in linhas:
            
        linha = float(linha)

        soma += linha 

    print('valores somados: {:.2f}'.format(soma))


        
        

if __name__ == '__main__':
    somar_valores()
    print(somar_valores)
            
            

