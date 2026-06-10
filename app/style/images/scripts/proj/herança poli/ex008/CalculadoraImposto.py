class CalculadoraImposto:
    def calcular(self, valor:int):
        valor = valor * 0.05 

class ImpostoArtigoLuxo(CalculadoraImposto):
    def calcular(self, valor:int):
        valor = valor * 0.20