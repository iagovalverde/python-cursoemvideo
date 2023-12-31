# SEPARANDO DIGITOS DE UM TEXTO
# Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

n = int(input('Digite um valor: [0 a 9999] '))
m = n // 1000
c = (n % 1000) // 100
d = (n % 100) // 10
u = n % 10

print(f'unidade: {u}'
    f'\ndezena: {d}'
    f'\ncentena: {c}'
    f'\nmilhar: {m}')

