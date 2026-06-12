from elevadorError import ElevadorSobrecarregadoError

class Elevador:
    def __init__(self, peso_pessoa:int):
        self.peso_pessoa = peso_pessoa

    def entrar_pessoa(self, peso_pessoa: int):
        peso_total = 0 
        if peso_total + peso_pessoa > 400:
          raise ElevadorSobrecarregadoError('Elevador sobreccaregado!')   
