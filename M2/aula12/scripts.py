# CONDICOES ANINHADAS

# if
# elif
# else

nome = input('Qual é o seu nome? ')
if nome == 'Iago':
    print('Que nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria':
    print(f'O nome {nome} é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {nome}')