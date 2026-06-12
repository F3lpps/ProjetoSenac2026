from ContaBlock import ContaBloqueadaError
class Autenticador:
    def fazer_login(self, senha_digitada: str):
        self.senha_digitada = senha_digitada
        senha_correta = "1234"
        tentativas = 0 

        if senha_digitada != senha_correta:
            tentativas = tentativas + 1 

        if tentativas == 3:
            raise ContaBloqueadaError('Conta Bloqueada! tente novamente mais tarde.')
        
        
