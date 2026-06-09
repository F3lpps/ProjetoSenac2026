class Jogador:
    nome:str = "joãozinho"
    pontuacao:int = 0 

    def __init__(self, d_centro:int):
        if d_centro < 5:
            self.pontuacao + 100

        if d_centro > 5 < 20:
            self.pontuacao + 50

        if d_centro > 20:
            self.pontuacao + 10
