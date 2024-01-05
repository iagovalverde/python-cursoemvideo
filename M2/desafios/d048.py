# SOMA IMPARES MULTIPLOS DE 3
# Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500

s = 0
for c in range(0, 500+1, 3):
    if c % 2 != 0:
        s += c
print(s)