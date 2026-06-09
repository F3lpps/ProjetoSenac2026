class Tamagotchi:
    nome:str
    fome:int = 50
    felicidade:int = 50

    def __init__(self, nome:str, fome:int, felicidade:int):
        self.nome = nome
        self.fome = fome
        self.felicidade = felicidade 

    def alimentar(self):
        if self.fome - 15 == 0:
            self.fome = 0 
            self.felicidade + 15

    def brincar(self):
        self.felicidade + 20 and self.fome + 10

        if self.felicidade >= 100:
            return self.felicidade == 50
