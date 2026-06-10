class Animal:
    def __init__(self, som_generico:str):
        self.som_generico = som_generico

    def emitir_som(self):
        return self.som_generico
        
    
class gato(Animal):
    def __init__(self, som:str):
        self.som = "miau!"

    def emitir_som(self):
        print(self.som)
    



        