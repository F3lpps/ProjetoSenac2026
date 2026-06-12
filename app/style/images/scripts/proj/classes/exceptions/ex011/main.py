from Instrumento import Instrumento
from guitarra import Guitarra
from Anatomiaerror import AnatomiaError

if __name__ == '__main__':

    tocar = Instrumento.tocar(Instrumento)
    tocar2 = Guitarra.tocar(Guitarra)

    try:
        tocar(Instrumento)
    except AnatomiaError as e:
        print(e)


    try:
        tocar2(Guitarra)
    except AnatomiaError as e:
        print(e)
