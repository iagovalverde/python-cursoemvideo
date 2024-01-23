# TRATANDO VARIOS VALORES v1.0
# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condiçao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0
contador = -1
soma = 0

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um numero [999 para parar]: '))
print(f'Foram digitados {contador} numeros. Com soma total de {soma}')