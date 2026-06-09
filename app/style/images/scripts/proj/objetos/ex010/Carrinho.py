class CarrinhoCompras:
    itens:list = {}
    precos:list = {}

    def __init__(self, itens:list, preços:list):
        self.itens = itens
        self.precos = preços

    def adicionar_item(self, nomeProduto:str, precoProduto:float):
        self.itens.append(nomeProduto)
        self.precos.append(precoProduto)

    def calcular_total(self, precoProduto):
            sum(self.preco.value())