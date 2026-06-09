class Termometro:
    temperatura_atual:float

    def __init__(self, temperatura_atual:float):
        self.temperatura_atual = temperatura_atual

        def aumentar(self, graus:float):
            self.temperatura_atual = self.temperatura_atual + graus 

        def diminuir(self, graus:float):
            self.temperatura_atual = self.temperatura_atual - graus 

        def alerta_clima(self):
            if self.temperatura_atual < 0:
                return (f"Congelando!")
            if self.temperatura_atual == 0 and 25:
                return (f"Agradável!")
            if self.temperatura_atual > 25:
                return ("Calorão!")