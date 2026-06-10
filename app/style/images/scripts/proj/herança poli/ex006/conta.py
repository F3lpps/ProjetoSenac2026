class Conta:
    saldo:int = 100


class ContaEstudante(Conta):
    def  render_bonus (self):
        self.saldo = self.saldo + 10
    

