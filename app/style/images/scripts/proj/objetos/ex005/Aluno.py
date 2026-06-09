class Aluno:
    nome:str
    notas:list[int]

    def __init__(self, nome:str, notas:list):
        self.nome = nome
        self.notas = notas 

        def calcular_media(self):
            soma: int = 0

            for nota in self.notas:
                soma = soma + nota 

                return soma / len(self.notas)
                

        def verificar_situacao(self):
            media = self.calcular_media()
            
            if media >= 7:
                return (f"Aprovado!")
            if media >= 5.0 < 7:
                return (f"recuperação") 
            else:
                return (f"Reprovado!")
     
