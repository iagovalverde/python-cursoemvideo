# PROGRESSAO ARITMETICA v2.0
# Refaça o DESAFIO 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while

primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razao da PA: '))
c = 1

while c <= 10:
    print(primeiro, end=' ')
    primeiro += razao 
    c += 1
print('FIM')