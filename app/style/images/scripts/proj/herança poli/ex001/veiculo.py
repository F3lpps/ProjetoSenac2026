class Veiculo:

    def __init__(self, marca: str, ano: int ):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__m(self, marca:str, ano:int):
        super().__init__(marca, ano)

    