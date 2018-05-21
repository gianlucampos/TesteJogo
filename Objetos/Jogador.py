from Css import Formatos

# define a estrutura do jogador 1
jogador = Formatos.turtle.Turtle()
jogador.shape(".template/ship2.gif")
jogador.up()
jogador.speed(0)
jogador.setheading(90)
jogador.setposition(0, -210)
velocidadeJogador = 15
