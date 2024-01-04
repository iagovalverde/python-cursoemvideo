# CLASSIFICANDO ATLETAS
# A confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 
# - Ate 9 anos: Mirim
# - Ate 14 anos: Infantil
# - Ate 19 anos: Junior
# - Ate 20 anos: Senior
# - Acima: Master

nascimento = int(input('Ano de nascimento: '))
idade = 2024 - nascimento
print(idade)
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 20:
    print('Senior')
else:
    print('Master')