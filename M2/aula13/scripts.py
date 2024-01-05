# ESTRUTURA DE REPETICAO FOR

for c in range(0,6):
    print('Oi')
print('Fim')
print('--------------------')

# Contagem regressiva 6 ate 0
for c in range(6, 0, -1):
    print(c)
print('--------------------')

# Contar de 0 ate 7 saltando 2
for c in range(0, 7, 2):
    print(c)

# Contagem opcional
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range (i, f+1, p):
    print(c)
print('Fim')
print('--------------------')

# Somatoria
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s+= n
print(s)
print('FIM')