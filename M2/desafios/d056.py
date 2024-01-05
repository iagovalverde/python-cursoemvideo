# ANALISADOR COMPLETO
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A media de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 21 anos

idades = 0
homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menores_21 = 0

for c in range(1, 5):
    print(f'--- {c}° PESSOA ---')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M / F]: ')

    idades += idade
    if sexo == 'M' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 21:
        mulheres_menores_21 += 1

media_idade = idades / 4

print(f'A media de idade do grupo é de: {media_idade} anos'
    f'\nO nome do homem mais velho é: {nome_homem_mais_velho} e tem {homem_mais_velho} anos'
    f'\n{mulheres_menores_21} mulher/es tem idade menor do que 21 anos')
