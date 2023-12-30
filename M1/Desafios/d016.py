# QUEBRANDO UM NUMERO
# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao Inteira,
# EX: Digite um numero: 6.127
# O numero 6.127 tem parte Inteira 6

from math import floor

n = float(input('Digite um numero Real: '))
n_inteiro = floor(n) 
print(f'O numero {n} tem a parte Inteira {n_inteiro}')