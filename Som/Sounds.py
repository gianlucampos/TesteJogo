from pygame import mixer
from time import sleep


def tiro():
    mixer.init()
    mixer.music.load('.som/pow.wav')
    mixer.music.play()
    soundtrack()


def sure():
    mixer.init()
    mixer.music.load('.som/test16.wav')
    mixer.music.play()
    sleep(1)
    soundtrack()


def soundtrack():
        mixer.init()
        mixer.music.load('.som/run.mp3')
        mixer.music.play()
