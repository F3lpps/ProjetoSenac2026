from playlist import Playlist 

if __name__ == '__ main __':

    Playlist.nome = Playlist.nome("Musicas topzera")
    Playlist.adicionar_musica("Creep")

    Playlist.remover_musica("From the start")

    print(Playlist.mostrar_playlist())
    


