from ContaBlock import ContaBloqueadaError
class Autenticador:
    def __init__(self):
        self.tentativas = 0
        self.senha_correta = "1234"

    def fazer_login(self, senha_digitada: str):
            if senha_digitada == self.senha_correta:
                print("Login realizado!")
            self.tentativas = 0
            return True
    
            if not senha_digitada == self.senha_correta:
                self.tentativas += 1
            print(f"senha incorreta! tente novamente")

            if self.tentativas >= 3:
                raise ContaBloqueadaError(f'Conta bloqueada! tente novamente mais tarde...')  

if __name__ == '__main__':

    autenticador = Autenticador()
    try:
        autenticador.fazer_login("4321") 
        autenticador.fazer_login("0000") 
        autenticador.fazer_login("9999") 
    except ContaBloqueadaError as e:
        print(f"Erro capturado: {e}")

        





       