# CONVERSOR DE BASES NUMERICAS
# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao: 
# - 1 para binario
# - 2 para octal
# - 3 para hexadecimal

numero = int(input('Digite um numero: '))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

opcao = int(input('Escolha a base de conversao: '
            '\n1 - binario'
            '\n2 - octal'
            '\n3 - hexadecimal'
            '\n'))

if opcao == 1: 
    print(f'O numero {numero} em binario é {binario}')
elif opcao == 2:
    print(f'O numero {numero} em octal é {octal}')
elif opcao == 3:
    print(f'O numero {numero} em hexadecimal é {hexadecimal}')