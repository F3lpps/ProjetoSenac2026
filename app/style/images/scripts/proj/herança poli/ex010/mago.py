from heroi import Heroi

class Mago(Heroi):
    PoderMagico:int

    def __init__(self, nome:str, vida:int, PoderMagico:int):
        self.PoderMagico = PoderMagico
        super.__init__()
        self.atacar = PoderMagico + 10 
