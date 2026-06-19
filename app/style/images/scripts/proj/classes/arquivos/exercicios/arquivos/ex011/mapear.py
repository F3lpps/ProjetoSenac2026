def mapear_paredes_planta(nome_arquivo: str):
    coordenadas = []
    
    with open(nome_arquivo, 'r') as arquivo:
        try:
            for linha_index, caractere in enumerate(arquivo.readlines()):
                for coluna_index, caractere in enumerate(arquivo.readlines()):
                    if caractere == '=':
                        coordenadas.append(coluna_index, linha_index)

        except FileNotFoundError:
                print(f'Arquivo não encontrado...')


        return coordenadas

       

if __name__ == '__main__':
    coordenadas = (
        '/app/style/images/scripts/proj/classes/arquivos/exercicios/arquivos/ex011/coordenadas_planta.csv')
    print(coordenadas)

        
            
            

            
            
            


    
       