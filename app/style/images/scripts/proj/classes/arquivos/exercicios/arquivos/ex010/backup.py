import shutil

def fazer_backup(nome_arquivo_original):
    with open(nome_arquivo_original, 'w') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            try:
                shutil.copy(nome_arquivo_original, 'dados_csv.bak')
                print(f'Backup realizado com sucesso!')
                
            except FileNotFoundError:
                print(f'Arquivo não encontrado.')
            except Exception:
                print('Erro')
            
        

