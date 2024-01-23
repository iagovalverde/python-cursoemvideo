# VALIDACAO DE DADOS
# Faca um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitaçao novamente até ter um valor correto.

sexo = input('Qual seu sexo? [m/f]: ')

while sexo != 'm' and sexo != 'f':
    print('[ERRO]')
    sexo = input('Qual seu sexo? [m/f]: ')

print('Fim')