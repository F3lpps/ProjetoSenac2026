def triangulo_base_altura(b: float, a: float):
    print(f"A área do triângulo é {b * a / 2}")

def temp_conversao(c: float):
    print(f"A temperatura em fahrenreit é {c / 5 * 9 + 32}")

def reais_conversao(r: float):
    print(f"O valor em dolares é {r / 5.03}")

def calc_salario_desconto(S: float):
    Sd = S - S*0.15
    return Sd

def Club_Felps(nome: str, idade: int):
    if nome == "felps" and idade >= 16:
        print("Voce é membro do clube!")
    else:
                print("Vaza daqui meo!")

def class_population(idade: int) -> str:
    if idade <= 12 and idade:
        return "Criança"
    if idade > 12 and idade < 18:
        return "Adolescente"
    else:
        return "peter ei nerd"


def eh_par(numero:int):
    if numero % 2:
        return True
    else:
        return False

def calcular_bonus(S:float, a_empresa:int):
    if a_empresa > 5:
        return S * 0.1 
    else:
        return S * 0.05    

def encontrar_maior(a: float, b: float, c: float):
    if a > b and a > c:
        return a
    if c > b and c > a:
        return c
    if b > c and b > a:
        return b   

def tipo_triangulo(lado1, lado2, lado3):
 if lado1 + lado2 > lado3:
            if lado2 + lado3 > lado1:
                                        lado1 + lado3 > lado2
            return "Equilátero"
            if lado1 + lado2 < lado3:
                return "Isto não é um triângulo"
            if lado1 + lado2 == lado3:
                return "Isósceles"
            if lado1 + lado2 + lado3 == lado1 != lado2 != lado3:
                return "Escaleno"

def aprovar_saque(saldo:float, valor_saque: float):
    if valor_saque <= saldo and valor_saque % 10 == 0:
        return True
    else:
        return False 

    frutas = ['Laranja','banana','berga','maça',]

def primeira_fruta(frutas: list):
        return primeira_fruta[0]

animais = ['Gato','Raposa','cachorro','Koala']
def ultimo_animal(animais: list):
        return ultimo_animal[-1]   

         

    


