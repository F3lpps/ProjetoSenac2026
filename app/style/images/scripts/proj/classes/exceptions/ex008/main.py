class Produto:
    nome:str ="Arnaldão"
    preco:float = -1

    def __init__(self, nome:str, preco:float):
        self.nome = self.nome
        self.preco = self.preco

        if self.preco <= 0:
            raise ValueError('Preço invalido!')
        
        if __name__ == '__main__':
            try:
                self.__init__ ()
            except ValueError as e:
                print(e)
                

    