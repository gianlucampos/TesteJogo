from Funcoes import Funcao_Janela, Funcao_Jogador, Funcao_Tiro
from Objetos.Janela import janela

# Teclas Movimento
janela.onkey(Funcao_Jogador.move_frente, "Up")
janela.onkey(Funcao_Jogador.move_tras, "Down")
janela.onkey(Funcao_Jogador.move_esquerda, "Left")
janela.onkey(Funcao_Jogador.move_direita, "Right")

# Atira
janela.onkey(Funcao_Tiro.atira, "space")

# Reseta a tela
janela.onkey(Funcao_Janela.reseta_tela, "r")

# Fecha o Jogo
janela.onkey(Funcao_Janela.tchau, "q")  # quit game

# inserir isso ao clicar no X
# janela.exitonclick()
# ou isso
# janela.bye()
