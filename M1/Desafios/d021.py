# TOCANDO UM MP3
# Faca um programa em Python que abra e reproduza o audio de um arquivo mp3

from pygame import mixer

mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
x = input('Curta o som')
