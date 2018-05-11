from Objetos.Tiro import tiro
from Objetos import Tiro


def move_bala():
    if Tiro.estado_tiro == "fogo":
        y = Tiro.tiro.ycor()
        y += 15
        tiro.sety(y)


def esconde_bala():
    if tiro.ycor() > 240:
        tiro.hideturtle()
        Tiro.estado_tiro = "pronto"
