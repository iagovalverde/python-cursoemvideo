# MAIOR E MENOR VALORES
# Faca um programa que leia tres numeros e mostre qual é o maior e qual é o menor.

# abc
# acb
# bac
# bca
# cab
# cba

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))

print(f'O maior é {max(a, b, c)}'
    f'\nO menor é {min(a, b, c)}')

# if ((a > b) and (a > c)):
#     if ((b > c)):
#         print(f'{a} é o maior'
#         f'{c} é o menor')
#     else:
#         print(f'{a} é o maior'
#         f'\n{b} é o menor')
# elif ((b > a) and (b > c)):
#     if (a > c):
#         print(f'{b} é o maior'
#         f'{c} é o menor')
#     else: 
#         print(f'{b} é o maior'
#         f'{a} é o menor')
# elif ((a > b)):
#     print(f'{c} é o maior'
#         f'{b} é o menor')
# else: 
#     print(f'{c} é o maior'
#         f'{a} é o menor')

