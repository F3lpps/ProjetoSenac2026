from Anatomiaerror import AnatomiaError

class Instrumento:
    def tocar(self):
        raise AnatomiaError('Classes abstratas não tocam som.')