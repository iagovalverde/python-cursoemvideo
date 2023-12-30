# SORTEANDO UM ITEM DA LISTA
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

from random import choice

print('Sorteio de Alunos')
alunos = input('Digite o nome dos alunos [a1, a2, a3...]: ').split(',')

print(f'O aluno escolhido foi {choice(alunos)}')

