# SEQUENCIA DE FIBONACCI v1.0
# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci.
# Ex: 0 _ 1 _ 1 _ 2 _ 3 _ 5 _ 8 _ 13 _ 21
#    ant atu prox
#        ante    atual

print('Sequencia de Fibonacci')

numero = int(input('Quantos termos voce quer mostrar? '))
contador = 2
anterior = 0
atual = 1

if numero == 1:
    print(f'{anterior} | Fim')
elif numero == 2:
    print(f'{anterior} -> {atual} | Fim', end=' ')
elif numero > 2:
    print(f'{anterior} -> {atual}', end=' ')
    while contador < (numero):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
        print(f'-> {proximo}', end=' ')
        contador += 1 
    print('| Fim')