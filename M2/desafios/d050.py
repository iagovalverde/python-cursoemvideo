# SOMA DOS PARES
# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

s = 0

for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
print(s)