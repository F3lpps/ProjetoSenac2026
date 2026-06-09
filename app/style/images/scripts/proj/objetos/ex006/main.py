from termometro import Termometro

if __name__ == '__main__':
    
    termometro = Termometro(20.0)
    
    termometro.diminuir(0)
    assert termometro.alerta_clima() == "Congelando"

    termometro.aumentar(40)
    assert termometro.alerta_clima() == "Agradável"

    termometro.aumentar(20)
    assert termometro.alerta_clima() == "Calorão!"