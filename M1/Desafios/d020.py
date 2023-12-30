# SORTEANDO UMA ORDEM NA LISTA
# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import sample

alunos = str(input('Digite o nome dos alunos [a1, a2, a3...]: '))
lista = alunos.split(',')
print(f'A ordem de alunos é: {sample(lista, 4)}')