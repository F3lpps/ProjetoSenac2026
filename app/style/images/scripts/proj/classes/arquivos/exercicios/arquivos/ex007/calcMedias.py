def calcular_media():
    with open('notas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        
    with open('medias_finais.txt', 'w') as arquivo2:
                
        for linha in linhas:
            if not linha.strip():
                 continue
            
            linha_limpa = linha.strip()
            notas = linha_limpa.split(',')

            nome = notas[0]
            nota1 = float(notas[1])
            nota2 = float(notas[2])
            media = (nota1 + nota2) / 2 

            print(f'Aluno: {nome} / Média: {media:.2f}', file=arquivo2) # 2f é um formato específico usado para formatar um número como um número de ponto flutuante arredondado para exatamente duas casas decimais, doc em W3Escolas.

if __name__ == '__main__':
    calcular_media()

        
            
        
             
             
             
             
             

        


        

    
        

        