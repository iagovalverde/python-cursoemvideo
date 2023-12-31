# PROCURANDO UMA STRING DENTRO DE OUTRA
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

n = input('Digite o nome: ')
n_minuscula = n.lower()
nome_silva = 'silva' in n_minuscula

if (nome_silva == True):
    print('O nome possui "SILVA"')
else: 
    print('O nome NAO possui "SILVA"')