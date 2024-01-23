# ESTRUTURA DE REPETICAO WHILE
# a vantagem em relacao ao FOR é que nao precisa de um range (o FOR precisa de um range)

# for c in range(1, 10):
#     print(c)
# print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

# -----------------------------------------------

resposta = 's'
while resposta == 's':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [s/n]'))
print('Fim')

# -----------------------------------------------

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} numeros impares')
