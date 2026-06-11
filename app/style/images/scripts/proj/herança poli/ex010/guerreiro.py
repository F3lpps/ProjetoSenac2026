from heroi import Heroi 

class Guerreiro(Heroi):
    forca_fisica:int

    def __init__(self, nome:int, vida:int, forca_fisica:int):
        self.forca_fisica = forca_fisica
        super.__init__()
        self.atacar = forca_fisica * 2