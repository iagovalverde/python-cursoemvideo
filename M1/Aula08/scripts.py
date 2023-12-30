# UTILIZANDO MODULOS
# math -> ceil, floor, trunc, pow, srqt, factorial

# import math (faz a importacao do modulo inteiro)
# from math import ceil, floor (importa apenas essas funcionalidades)

from math import sqrt, ceil

n = int(input('Digite um numero: '))
raiz = sqrt(n)
print(f'A raiz quadrada de {n} é {ceil(raiz)}')
