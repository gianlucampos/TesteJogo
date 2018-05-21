from Objetos import Bola, Jogador, Tiro, Janela
JanelaAtiva = True


def tchau():
    global JanelaAtiva
    JanelaAtiva = False


def reseta_tela():
    Janela.janela.resetscreen()
    Jogador.jogador.up()
    Jogador.jogador.speed(0)
    Jogador.jogador.setheading(90)
    Jogador.jogador.setposition(0, -210)

    Tiro.tiro.shape("triangle")
    Tiro.tiro.color("red")
    Tiro.tiro.shapesize(0.5, 0.5)
    Tiro.tiro.penup()
    Tiro.tiro.setheading(90)
    Tiro.tiro.hideturtle()
    Tiro.tiro.penup()
    Tiro.tiro.setposition(0, -210)
    Bola.bola.penup()
    Bola.bola.color("yellow")
