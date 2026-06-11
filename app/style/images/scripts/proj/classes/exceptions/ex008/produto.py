class Produto:
    nome:str ="Arnaldão"
    preco:int = 20.00

    def __init__(self, nome:str, preco:int):
        self.nome = self.nome
        self.preco = self.preco

        if self.preco <= 0:
            raise ValueError('Preço invalido!')

    