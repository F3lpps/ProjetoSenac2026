class Carro:

    modelo:str
    ano:int
    odometro:float

    def __init__(self, modelo:str, ano:int, odometro:int):
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def viajar(self, distancia:int):
        self.distancia + self.odometro
        if self.distancia < 0:
            return (f"Nada foi alterado.")

