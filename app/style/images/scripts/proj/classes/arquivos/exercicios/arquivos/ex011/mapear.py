def mapear_paredes_planta(nome_arquivo: str):
    coordenadas = []
    
    with open(nome_arquivo, 'r') as arquivo:
        try:
            for coluna_index, caractere in enumerate(arquivo):
                if caractere == '=':
                    coordenadas.append(coluna_index)

        except FileNotFoundError:
            print(f'Arquivo não encontrado...')

if __name__ == '__main__':
    mapear_paredes_planta('coordenadas_planta.csv')

        
            
            

            
            
            


    
       