from pygame import mixer


def tiro():
    mixer.init()
    mixer.music.load('.som/pow.wav')
    mixer.music.play()


def sure():
    mixer.init()
    mixer.music.load('.som/test16.wav')
    mixer.music.play()
