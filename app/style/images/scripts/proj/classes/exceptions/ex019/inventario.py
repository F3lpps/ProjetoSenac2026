from Fullbackpack import InventarioCheioExceptionError
from ItemInutilException import ItemInutilExceptionError
from Item import Espada
from Item import Pocao
from Item import Item 
from Item import PedraComum

class Inventario:

    objetos:list

    def __init__(self):
        self.objetos = []

    def guardar_item(self, objeto_item):

        if not isinstance(objeto_item, Item):
            raise TypeError(f'Isto não é um item valido.')
        
        if isinstance(objeto_item, PedraComum):
            raise ItemInutilExceptionError(f'Item não necessário!')
        
        if len(self.objetos) >= 3:
            raise InventarioCheioExceptionError(f'Seu inventário está cheio!') 
        
        if isinstance(objeto_item, Item):
            self.objetos.append(objeto_item)

if __name__ == '__main__':  

    meu_inventario = Inventario()
    item1 = Espada()
    item2 = Pocao()
    item3 = PedraComum()

    try: 
        print("Guardando Espada...")
        meu_inventario.guardar_item(item1)
        print("Guardando Pedra Comum...")
        meu_inventario.guardar_item(item3)
        
    except ItemInutilExceptionError as e:
        print(f"Item desnecessário!")