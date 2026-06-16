class Playlist:
    nome:str
    musicas:list

    def __init__(self, nome:str, musicas:list):
        self.nome = nome
        self.musicas = musicas

        def adicionar_musica(self, nome_musica:str):
            musicas.append(nome_musica)
            print (f"Musica adicionada!")

        def remover_musica(self, nome_musica):
            if nome_musica in musicas:
                musicas.remove(nome_musica)

            if nome_musica not in musicas:
                return (f"Música não encontrada.")
            
        def mostrar_playlist(self):
            print(nome) and print(musicas)

            

