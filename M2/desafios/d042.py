# ANALISANDO TRIANGULOS v2.0
# Refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado: 
# - Equilatero: todos os lados iguais
# - Isosceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))

if (a == b) or (b == c):
    if (a == c):
        tipo = 'equilatero'
    elif (a != c):
        tipo = 'isosceles'
elif (a != b and a != c):
    tipo = 'escaleno'


if ((a > b + c) or (b > a + c) or (c > a + b)):
    print(f'As retas {a}, {b} e {c} NAO PODEM formar um triangulo')
else:
    print(f'As retas {a}, {b} e {c} FORMAM um triangulo {tipo}')

