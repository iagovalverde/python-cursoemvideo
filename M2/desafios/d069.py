# ANALISE DE DADOS DO GRUPO
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou nao continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos

print('CADASTRE UMA PESSOA')
print('=-' * 10)

maior_idade = homens = mulheres_menos_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = resposta = ' '
    while sexo not in 'MF': 
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
        maior_idade += 1
    
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres_menos_20 += 1

    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
    
print(f'A) {maior_idade} pessoas maiores de 18 anos foram cadastradas'
    f'\nB) {homens} homens foram cadastrados'
    f'\nC) {mulheres_menos_20} mulheres menores de 20 anos foram cadastradas')