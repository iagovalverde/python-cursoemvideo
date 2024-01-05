# CONTAGEM REGRESSIVA
# Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize

for c in range(10, 0, -1):
    print(c)
    sleep(1.0)
print(emojize(':sparkler::fireworks:' * 8))
print(' FELIZ ANO NOVO '.center(32, '*'))