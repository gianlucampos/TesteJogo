import Bola
import Tiro
import Teclas


# main do jogo
while True:
    x = Bola.bola.xcor()
    x += Bola.bolavelocidade
    if Bola.bola.xcor() > 240:
        x = 240
        Bola.bolavelocidade *= -1

    if Bola.bola.xcor() < -240:
        x = -240
        Bola.bolavelocidade *= -1
    Bola.bola.setx(x)

    # move bala
    if Tiro.estado_tiro == "fogo":
        y = Tiro.tiro.ycor()
        y += 15
        Tiro.tiro.sety(y)

    # esconde bala
    if Tiro.tiro.ycor() > 240:
        Tiro.tiro.hideturtle()
        Tiro.estado_tiro = "pronto"
