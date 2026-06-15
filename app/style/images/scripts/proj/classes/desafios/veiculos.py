from veiculo import Veiculo

class Onibus(Veiculo):
    def __init__(self):
        super().__init__()
        self.placa = ""
        self.peso = ""
        self.cor = ""
        self.condutor = "Aldoir"
        self.capacidade = 23
       


class Van(Veiculo):
    def __init__(self):
        super().__init__()
        self.placa = ""
        self.peso = ""
        self.cor = ""
        self.condutor = "Arnaldo"
        self.capacidade = 12
        

class Carro(Veiculo):
   def __init__(self):
       super().__init__()
       self.placa = ""
       self.peso = ""
       self.cor = ""
       self.condutor = "Vanderlei"
       self.capacidade = 5
       

