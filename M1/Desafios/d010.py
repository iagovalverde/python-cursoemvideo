# CONVERSOR DE MOEDAS
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
# Considere US$1,00 = R$3,27

reais = float(input('Digite quantos reais voce possui: R$'))

dolares = reais / 3.27
print(f'Com R${reais:.2f} voce pode comprar US${dolares:.2f}')