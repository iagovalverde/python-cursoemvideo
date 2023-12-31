# VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO"

cidade = input('Digite o nome da cidade: ')
inicio = cidade[:5].lower()
nome_santo = 'santo' in inicio

if(nome_santo == True):
    print('A cidade inicia com nome "Santo"')
else:
    print('A cidade NAO inicia com nome "Santo"')