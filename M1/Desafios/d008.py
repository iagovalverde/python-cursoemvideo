# CONVERSOR DE MEDIDAS
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

valor = float(input('Digite um valor (m): '))
centimetros = valor * 100
milimetros = valor * 1000
print(f'O valor {valor:.0f}m tem {centimetros:.0f}cm e {milimetros:.0f}mm')