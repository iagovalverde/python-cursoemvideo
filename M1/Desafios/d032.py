# ANO BISSEXTO
# Faca um programa que leia um ano qualquer e mostre se ele é Bissexto

ano = int(input('Digite um ano: '))
if (ano % 4 == 0):
    print(f'O ano de {ano} é bissexto')
else: 
    print(f'O ano de {ano} NAO é bissexto')