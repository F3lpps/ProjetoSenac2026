class Dispositivo:
    nome:str

    def __init__(self, nome:str):
        self.nome = nome 

class Celular(Dispositivo):
    nome:str
    bateria:int

    def __init__(self, nome:str, bateria:int):
        super().__init__(nome)
