# PROGRESSAO ARITMETICA
# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.

primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razao da PA: '))
decimo = primeiro + (10-1) * razao

for c in range(primeiro, decimo + razao , razao):
    print(c, end=" ")
print('FIM')