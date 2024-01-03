# ANALISANDO TRIANGULO v1.0
# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.

# condicao de existencia -> a < b + c

a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))

if ((a > b + c) or (b > a + c) or (c > a + b)):
    print(f'As retas {a}, {b} e {c} NAO PODEM formar um triangulo')
else: 
    print(f'As retas {a}, {b} e {c} FORMAM um triangulo')