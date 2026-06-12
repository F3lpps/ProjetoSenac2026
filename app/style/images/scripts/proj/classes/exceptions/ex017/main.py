class Usuario:
    pass

class Comum(Usuario):
    pass

class Admin(Usuario):
    pass 

    def deletar_bancoDados(usuario_objeto):
        if isinstance(usuario_objeto, (Admin)):
            raise PermissionError('Você deve ser Admin para executar esta operação')
        
if __name__ == '__main__':
    comum = Comum()
    admin = Admin()

    


    