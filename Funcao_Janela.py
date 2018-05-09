import Janela
import Jogador
import Tiro
import Bola


def tchau():
    Janela.janela.bye()

def reseta_tela():
    Janela.janela.resetscreen()
    Jogador.jogador.shape("turtle")
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
