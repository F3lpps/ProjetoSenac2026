## Ex; Aula 4

## Ex: 001

class Pessoa:
    nome:str = "Fulaninho"
    idade:int = 12

    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade 

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, minha idade é {self.idade}"


