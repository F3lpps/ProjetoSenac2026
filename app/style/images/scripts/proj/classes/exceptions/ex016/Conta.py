from SaldoError import SaldoInsuficienteError  
class ContaBancaria:
    def __init__(self, saldo: float):
        self.saldo = 100

    def sacar(self, valor: float):
        if valor > self.saldo:
            diferença = valor - self.saldo
            raise SaldoInsuficienteError
        
        self.saldo -= valor 
        return f"saque realizado! novo saldo: {self.saldo}"
            

