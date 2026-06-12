from idadeError import IdadeinvalidaError

class Cadastrar_eleitor:
    def __init__(self, idade:int):
        self.idade = idade

    def cadastrar_eleitor(idade:int):
        if idade < 16:
            raise IdadeinvalidaError('Idade invalida!')
    print("Eleitor cadastrado com sucesso!")
      
    if __name__ == '__main__':
        cadastrar_eleitor(12)
        

