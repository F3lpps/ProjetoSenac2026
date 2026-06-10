class Empresa:
    nome:str = "marquespan"
    funcionarios:list

    def __init__(self, nome:str, funcionarios:list):
        self.nome = nome
        self.funcionarios = funcionarios

    def contratar(self, funcionario:str):
        self.funcionarios.append(funcionario)

    def demitir(self, funcionario:str):
        self.funcionarios.remove(funcionario)

    def verificar_funcionario(self, funcionario:str):
        if funcionario in self.funcionarios:
            return True
        else:
            return False