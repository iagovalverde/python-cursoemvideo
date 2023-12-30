# CATETOS E HIPOTENUSA
# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))
hipotenusa = hypot(cateto1, cateto2)

print(f'Com catetos de valor {cateto1} e {cateto2} a hipotenusa é de {hipotenusa}')