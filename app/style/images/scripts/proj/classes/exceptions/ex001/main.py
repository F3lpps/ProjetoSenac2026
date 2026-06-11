from ex001 import Divisao 

import traceback

if __name__ == '__main__':

    divisao = Divisao()

    try:
        divisao.dividir_numeros(1, 0)
    except ZeroDivisionError as e:
        print(traceback.format_exc())

    finally:
        b = int(input('digite um novo número maior que zero: '))
        print(divisao.dividir_numeros(1,b))