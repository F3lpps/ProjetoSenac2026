from veiculo import Veiculo

class Onibus(Veiculo):
    def __init__(self, placa: str, peso: float, cor: str, condutor: str):
        super().__init__(placa, peso, cor, condutor, capacidade=45, tamanho=12.0)
        
       


class Van(Veiculo):
    def __init__(self, placa: str, peso: float, cor: str, condutor: str):
        super().__init__(placa, peso, cor, condutor, capacidade=12, tamanho=6.0)
        
        

class Carro(Veiculo):
   def __init__(self, placa: str, peso: float, cor: str, condutor: str):
       super().__init__(placa, peso, cor, condutor, capacidade=5, tamanho=4.5)
       
       

