from vaga import Vaga
from veiculos import Onibus
from veiculos import Carro
from veiculos import Van


class VagaOnibus(Vaga):
    def __init__(self):
        super().__init__()
        self.veiculo = Onibus
        self.capacidade: int = 0

class VagaCarro(Vaga):
    def __init__(self):
        super().__init__()
        self.veiculo = Carro
        self.capacidade: int = 0
        self.h_entrada = None

class VagaVan(Vaga):
    def __init__(self):
        super().__init__()
        self.veiculo = Van 
        self.capacidade: int = 0
        self.h_entrada: int = 0 

    