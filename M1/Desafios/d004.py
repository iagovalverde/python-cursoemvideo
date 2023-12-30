# DISSECANDO UMA VARIAVEL
# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

n = input('Digite algo: ')
print(n)
print(f'O tipo primitivo é: {type(n)}')
print(f'É numerico? {n.isnumeric()}')
print(f'É alfanumerico? {n.isalnum()}')
print(f'É alfabetico? {n.isalpha()}')
print(f'Esta em minusculas? {n.islower()}')
print(f'Esta em maiusculas? {n.isupper()}')
print(f'Esta capitalizada? {n.istitle()}')
print(f'Só tem espacos? {n.isspace()}')