# JOGO DA ADIVINHACAO v1.0
# Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu.

from random import choice

print('O Computador pensará em um número de 0 a 5, tente adivinhar.')
n = int(input('Qual valor o computador pensou? '))
lista = [0, 1, 2, 3, 4, 5]
pensado = choice(lista)
print(f'O numero pensado foi {pensado}')
if (n == pensado):
    print('Parabéns, voce acertou!')
else: 
    print('Tente outra vez')