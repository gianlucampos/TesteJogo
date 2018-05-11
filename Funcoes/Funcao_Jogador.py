from Objetos import Jogador


def move_frente():
    Jogador.jogador.up()
    Jogador.jogador.forward(30)


def move_tras():
    Jogador.jogador.up()
    Jogador.jogador.backward(30)


def move_esquerda():
    x = Jogador.jogador.xcor()
    x -= Jogador.velocidadeJogador
    if x < -210:
        x = -210
    Jogador.jogador.setx(x)


def move_direita():
    x = Jogador.jogador.xcor()
    x += Jogador.velocidadeJogador
    if x > 240:
        x = 240
    Jogador.jogador.setx(x)
