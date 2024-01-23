# MAIOR E MENOR VALORES
# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execuçao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.

resposta = 's'
contador = soma = media = maior = menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um numero: '))
    soma += numero
    contador += 1

    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        
        if numero < menor:
            menor = numero
    
    resposta = input('Deseja continuar? [s/n] ')

media = soma / contador
print(f'A media entre todos os valores foi de {media}'
    f'\nO maior valor foi: {maior}'
    f'\nO menor valor foi: {menor}')