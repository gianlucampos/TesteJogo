from Som import Sounds
from Objetos import Jogador, Tiro


def atira():
    global estado_tiro
    if Tiro.estado_tiro == "pronto":
        Sounds.tiro()
        Tiro.estado_tiro = "fogo"
        x = Jogador.jogador.xcor()
        y = Jogador.jogador.ycor() + 30
        Tiro.tiro.setposition(x, y)
        Tiro.tiro.showturtle()

