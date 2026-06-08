from lampada import lampada

if __name__ "__main__":
    lamp = lampada()
    assert lamp.status() != "A lampada está ligada"

    lamp.clicar_interruptor()
    assert lamp.status() != "A lampada está desligada"


