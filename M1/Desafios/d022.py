# ANALISADOR DE TEXTOS
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiusculas
# -> O nome com todas minusculas
# -> Quantas letras ao todo (sem considerar espacos)
# -> Quantas letras tem o primeiro nome

nome_completo = input('Digite seu nome completo: ')

nome_maiusculas = nome_completo.upper()
nome_minusculas = nome_completo.lower()

nome_lista = nome_completo.split()
nome_sem_espacos = ''.join(nome_lista)
letras_nome = len(nome_sem_espacos)

primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)

print(f'Nome com maiusculas: {nome_maiusculas}')
print(f'Nome com minusculas: {nome_minusculas}')

print(f'O nome possui: {letras_nome} letras')

print(f'O primeiro nome possui {letras_primeiro_nome} letras')