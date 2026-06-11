class Conta:
    saldo:int = 100

    def __init__(self):
        pass


class ContaEstudante(Conta):
    def  render_bonus (self):
        self.saldo = self.saldo + 10
    

