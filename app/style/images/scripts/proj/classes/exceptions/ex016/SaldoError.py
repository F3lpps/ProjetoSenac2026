class SaldoInsuficienteError(Exception):

    def __init__(self, saldofaltante: float):
        super().__init__(f"saldo insuficiente para realizar o saque, restam {saldofaltante} para realizar o saque.")
        self.saldo_faltante = saldofaltante



