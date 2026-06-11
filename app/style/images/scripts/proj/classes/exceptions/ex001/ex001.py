class Divisao:
    def dividir_numeros(self, a:int, b:int):
        if b == 0:
            raise ZeroDivisionError("Não é possivel dividir por zero.")
        return a/b