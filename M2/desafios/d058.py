# JOGO DA ADIVINHAÇAO v2.0
# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import choice

print('O Computador pensará em um número de 0 a 10, tente adivinhar.')

contador = 1
numero_usuario = int(input('Qual valor o computador pensou? '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_computador = choice(lista)
print(f'Computador: {numero_computador}')

while numero_usuario != numero_computador:
    numero_usuario = int(input('Tente outra vez: '))
    numero_computador = choice(lista)
    contador += 1
    print(f'Computador: {numero_computador}')

print(f'Voce acertou na {contador}° tentativa! Parabéns!!!')