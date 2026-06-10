class AgendaContatos:

    nomes:list
    telefones:list

    def __init__(self, nomes:list, telefones:list):
        self.nomes = nomes
        self.telefones = telefones

    def salvar_contato(self, nome:str, telefone:str):
        self.nomes.append(nome)
        self.telefones.append(telefone)

         
    def buscar_telefone(self, nome_pesquisado:str):
        if nome_pesquisado in self.nomes:
            return nome_pesquisado in self.nomes
        

        if nome_pesquisado in self.nomes:
            indice = self.nomes.index(nome_pesquisado)
            return self.telefones[indice]

        else:
            return (f"Contato não encontrado.")
