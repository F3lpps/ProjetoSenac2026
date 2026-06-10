class Instrumento:
    def tocar(self):
        pass

class Violao(Instrumento):
    def tocar(self):
        return (f"Acorde de violão")
    
class Flauta(Instrumento):
    def tocar(self):
        return (f"Melodia doce")
    
class Bateria(Instrumento):
    def tocar(self):
        return (f"Batida forte")