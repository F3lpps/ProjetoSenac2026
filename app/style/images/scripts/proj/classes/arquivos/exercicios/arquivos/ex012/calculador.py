def analisar_dimensoes_casa(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        

        planta = [linha.rstrip('\n') for linha in linhas]

        if not planta or all(len(linha)) == 0:
            raise ValueError('a planta encontra-se vazia.')
        
    perimetro = 0 
    area_util = 0
    total_linhas = 0 

    for i, linha in enumerate(planta):
        perimetro += linha.count('=')

    if i != 0 and i == total_linhas -1:
        primeiro_igual = linha.find('=')
        ultimo_igual = linha.rfind('=')

    if primeiro_igual != -1 and ultimo_igual != -1 and primeiro_igual != ultimo_igual:
        counteudo_interno = linha[primeiro_igual + 1: ultimo_igual]
        area_util += len(counteudo_interno)



        
 

