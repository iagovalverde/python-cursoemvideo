# TABUADA v3.0
# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o numero solicitado for negativo.

numero = int(input('Quer ver a tabuada de qual valor? '))
print('-' *33)
c = 0

while numero >= 0:
    while c <= 10:
        print(f'{numero} x {c} = {numero * c}')
        c += 1
    c = 0
    print('-' *33)
    numero = int(input('Quer ver a tabuada de qual valor? '))
print('Programa TABUADA encerrado. Volte sempre!')