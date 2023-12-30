# ALUGUEL DE CARRO
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

km_percorridos = float(input('Quantos Km foram percorridos?'))
dias_alugados = int(input('Por quantos dias foi alugado?'))

preco = (dias_alugados * 60) + (km_percorridos * 0.15)
print(f'O valor do carro alugado por {dias_alugados}dias, tendo rodado {km_percorridos}Km é de R${preco}')