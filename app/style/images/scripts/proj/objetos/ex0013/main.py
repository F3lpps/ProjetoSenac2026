from agendaC import AgendaContatos

if __name__ == '__main__':
   

   minha_agenda = AgendaContatos("Alana", "Brunão")

minha_agenda.salvar_contato("Alana", "9999-1111")

print(minha_agenda.buscar_telefone("Alana"))    

   