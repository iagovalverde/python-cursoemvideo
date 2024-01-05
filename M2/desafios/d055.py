# MAIOR E MENOR DA SEQUENCIA
# Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 1000**1000

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}° pessoa [Kg]: '))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso foi: {maior_peso}Kg'
    f'\nO menor peso foi: {menor_peso}Kg')