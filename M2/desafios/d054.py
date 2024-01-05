# DETECTOR DA MAIORIDADE
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas já sao maiores.

maiores = 0
menores = 0

for pessoas in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = 2024 - nascimento
    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f'Das 7 pessoas: '
    f'\n{menores} sao menores'
    f'\n{maiores} sao maiores')