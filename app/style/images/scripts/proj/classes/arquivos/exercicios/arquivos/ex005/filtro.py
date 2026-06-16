def filtrar_erros():
    arquivo = open('sistema.log', 'r')
    with open('sistema.log', 'r') as arquivo:
        linhas = arquivo.readlines()

    Erro = open('alerta_erros.txt', 'a')

    for linha in linhas:
        if linha.startswith('ERROR'):
            Erro.append(linha)

        with open('alerta_erros.txt', 'r'):
            Erro.write(linha)




    
        

