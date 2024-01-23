# CALCULO DO FACTORIAL
# Faça um programa que leia um numero qualquer e mostre o seu fatorial (while e for)
# Ex: 5! = 5x4x3x2x1 = 120
# Ex: 3! = 3x2x1 = 6

# ----------------------------------------
# USANDO WHILE

num = int(input('Digite um numero: '))
contador = num
factorial = 1

print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    factorial *= contador
    contador -= 1
print(factorial)

# ----------------------------------------
# USANDO FOR

num = int(input('Digite um numero: '))
contador = num
factorial = 1

print(f'Calculando {num}! = ', end='')
for contador in range(1, num + 1):
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    factorial *= contador
    contador -= 1
print(factorial)

