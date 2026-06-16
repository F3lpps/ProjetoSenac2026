from veiculos import Onibus
from veiculos import Carro
from veiculos import Van

class Vaga:
    def __init__(self):
        self.veiculo = None
        self.capacidade: int = 0
        self.h_entrada = None
        self.tamanho_maximo:float 

    def esta_ocupada(self) -> bool:
        return self.veiculo is not None
        

class VagaOnibus(Vaga):
    def __init__(self):
        super().__init__(self.tamanho_maximo==15.00)
        

class VagaCarro(Vaga):
    def __init__(self):
        super().__init__(self.tamanho_maximo==5.50)
       

class VagaVan(Vaga):
    def __init__(self):
        super().__init__(self.tamanho_maximo==7.50)
         

    
