from Comandos import Teclas
from Movimento.M_bola import move_bola
from Movimento.M_tiro import move_bala
from Eventos.Tiro_colisao import is_colisao
from Objetos import Bola, Tiro
import threading
from Som import Sounds
from time import sleep


def som():
        print("rola")
        thread_1 = threading.Thread(target=Sounds.soundtrack(), name="som")
        thread_1.start()
        # sleep(5)


# main do jogo
def main():
    i = 0
    while Teclas.Funcao_Janela.JanelaAtiva:
        is_colisao(Tiro.tiro, Bola.bola)
        move_bola()
        move_bala()
        if i == 0:
            som()
        print(threading.active_count())
        if not i > 0:
            i += 1
        print(i)


if __name__ == '__main__':
    main()
