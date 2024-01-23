# ESTATISTICAS EM PRODUTOS
# Crie um programa que leia o nome e o preco de varios produtos. O programa deverá perguntar se o usuario vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print('-' * 20)
print('LOJA SUPER BARATAO')
print('-' * 20)

total = 0
contador_mais_1000 = 0
flag_menor_preco = 0
menor_preco = 0
produto_menor_preco = ''

while True:
    resposta = ' '

    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))

    total += preco

    if preco > 1000:
        contador_mais_1000 += 1

    if flag_menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        produto_menor_preco = nome_produto
        flag_menor_preco = 1

    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'A) Total gasto: R${total}'
    f'\nB) {contador_mais_1000} produtos custaram mais de R$1000'
    f'\nC) Produto mais barato foi {produto_menor_preco} custando R${menor_preco}')