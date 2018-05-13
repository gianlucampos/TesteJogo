from Comandos import Teclas
from Movimento.M_bola import move_bola
from Movimento.M_tiro import move_bala, esconde_bala
from Eventos.Tiro_colisao import is_colisao
from Objetos import Bola, Tiro

# main do jogo
while Teclas.Funcao_Janela.JanelaAtiva:
    is_colisao(Tiro.tiro, Bola.bola)
    move_bola()
    move_bala()
    esconde_bala()
