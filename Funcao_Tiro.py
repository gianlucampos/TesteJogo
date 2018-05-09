import Sounds
import Tiro
import Jogador

def atira():
    Sounds.tiro()
    global estado_tiro
    if Tiro.estado_tiro == "pronto":
        Tiro.estado_tiro = "fogo"
    x = Jogador.jogador.xcor()
    y = Jogador.jogador.ycor() + 30
    Tiro.tiro.setposition(x, y)
    Tiro.tiro.showturtle()
