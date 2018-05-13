from Objetos import Bola, Tiro
import time
import math
from Som.Sounds import sure


# colisao se a bala e a bola estiverem no mesmo espaço
# def colisao():
#     xbola = Bola.bola.xcor()
#     ybola = Bola.bola.ycor()
#     xtiro = Tiro.tiro.xcor()
#     ytiro = Tiro.tiro.ycor()
#     if int(xbola) == int(xtiro) & int(ybola) == int(ytiro):
#         print("KABOOOOOOOOOOOOOOOOOOOOOOOM")
#         time.sleep(1)


# Calcula se a area ocupada entreas cordenadas do tiro e bala, usando teorema de pitagoras
def colisao2(tiro, bola):
    distancia = math.sqrt(math.pow(tiro.xcor() - bola.xcor(), 2) + math.pow(tiro.ycor() - bola.ycor(), 2))
    if distancia < 15:
        print("Pitagoras atingiu")
        return True
    else:
        return False


def is_colisao(tiro, bola):
    if colisao2(tiro, bola):
        tiro.hideturtle()
        tiro.estado_tiro = "pronto"
        tiro.setposition(0, -400)
        bola.setposition(0, 100)
        sure()
