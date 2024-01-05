# TABUADA v2.0
# Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for
# 1 x 2 = 2

n = int(input('Digite um numero: '))
print(f'Tabuada do {n}')
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
print('FIM')

