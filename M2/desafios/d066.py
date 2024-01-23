# VARIOS NUMEROS COM FLAG
# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condiçao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = contador = soma = 0

while numero != 999:
    soma += numero
    contador += 1 
    numero = int(input('Digite um valor (999 para parar): '))
print(f'A soma dos {contador} valores foi {soma}')