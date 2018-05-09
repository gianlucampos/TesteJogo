import Funcao_Janela
import Funcao_Jogador
import Funcao_Tiro
import Janela


# Teclas
Janela.janela.onkey(Funcao_Jogador.move_tras, "Down")
Janela.janela.onkey(Funcao_Jogador.move_frente, "Up")
Janela.janela.onkey(Funcao_Jogador.move_esquerda, "Left")
Janela.janela.onkey(Funcao_Jogador.move_direita, "Right")
Janela.janela.onkey(Funcao_Janela.tchau, "q")
Janela.janela.onkey(Funcao_Janela.reseta_tela, "r")
Janela.janela.onkey(Funcao_Tiro.atira, "space")
# Janela.mainloop()
