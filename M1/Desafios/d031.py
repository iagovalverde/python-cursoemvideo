# CUSTO DA VIAGEM
# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da passagem, cobrando R$0,50 por Km para viagens de ate 200km e R$0,45 para viagens mais longas.

d = float(input('Digite a distancia da viagem: '))
if (d <= 200):
    valor = 0.5 * d
else: 
    valor = 0.45 * d
print(f'A viagem de {d}Km terá custo de R${valor}')