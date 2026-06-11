def validar_usuario(nome:str):
    if nome == "" or len < 3:
        raise ValueError('Insira pelo menos quatro caracteres')
    
    else: 
        print("usuario valido")

    if __name__ == '__main__':
       
        validar_usuario("")
