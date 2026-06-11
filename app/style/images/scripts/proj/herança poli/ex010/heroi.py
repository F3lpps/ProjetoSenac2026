class Heroi:
    nome:str
    vida:int

    def __init__(self, nome:str, vida:int):
        self.vida = vida
        self.nome = nome

    def atacar(self):
        return(f"Não há arma.")