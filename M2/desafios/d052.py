# NUMEROS PRIMOS
# Faca um programa que leia um numero inteiro e diga se ele é ou nao um numero primo.

n = int(input('Digite um numero: '))
primo = True

for c in range(2, n):
    if n % c == 0:
        primo = False

if primo:
    print(f'O numero {n} é primo')
else:
    print(f'O numero {n} NAO é primo')