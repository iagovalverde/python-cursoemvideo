# PEDRA, PAPEL OU TESOURA
# Crie um programa que faca o computador jogar Jokenpo com voce.

# pedra - papel
# tesoura - pedra
# papel - tesoura
# tesoura - papel
# pedra - tesoura
# papel - pedra

from random import choice

usuario = input('pedra, papel ou tesoura? ')
opcoes = ['pedra', 'papel', 'tesoura']
pc = choice(opcoes)
print(pc)

if (usuario == 'pedra' and pc == 'papel') or (usuario == 'tesoura' and pc == 'pedra') or (usuario == 'papel' and pc == 'tesoura'):
    print(f'Usuario: {usuario}'
        f'\nPc: {pc}'
        f'\nVoce PERDEU')
elif ((usuario == 'tesoura' and pc == 'papel') or (usuario == 'pedra' and pc == 'tesoura') or (usuario == 'papel' and pc == 'pedra')):
    print(f'Usuario: {usuario}'
        f'\nPc: {pc}'
        f'\nVoce VENCEU')