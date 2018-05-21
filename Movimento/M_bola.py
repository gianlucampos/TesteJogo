from Objetos.Bola import bola
from Objetos import Bola


def move_bola():
    x = bola.xcor()  # posicao (238)
    x += Bola.bolavelocidade  # posicao + velocidade (236)
    if bola.xcor() > 238:
        x = 238
        Bola.bolavelocidade *= -1
    if bola.xcor() < -238:
        x = -238
        Bola.bolavelocidade *= -1
    bola.setx(x)
