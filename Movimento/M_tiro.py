from Objetos import Tiro
from Objetos.Tiro import tiro


def move_bala():
    # if Tiro.estado_tiro == "fogo":
        y = Tiro.tiro.ycor()
        y += 15
        tiro.sety(y)
        if tiro.ycor() > 270:
            tiro.hideturtle()
            Tiro.estado_tiro = "pronto"


# def esconde_bala():
#     if tiro.ycor() > 270:
#         tiro.hideturtle()
#         Tiro.estado_tiro = "pronto"
