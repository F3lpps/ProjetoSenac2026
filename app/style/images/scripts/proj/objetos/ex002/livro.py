class Livro:
    titulo:str = "Lord of the mysteries"
    autor:str = "Cuttefish that loves dying"
    quantidade_copias:int = "10000"

    def __init__(self, titulo:str, autor:str, quantidade_copias:int):
        self.titulo = titulo
        self.autor = autor 
        self.quantidade_copias = quantidade_copias

    def vender(self):
        if self.quantidade_copias > 0:
          self.quantidade_copias = self.quantidade_copias - 1
        return self.quantidade_copias
    print(f"venda realizada! menos {quantidade_copias}")

    def reabastecer(self, numero:int):
        self.quantidade_copias = self.quantidade_copias + numero

            






        