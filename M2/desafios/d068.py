# JOGO DO PAR OU IMPAR
# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint
soma = contador = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    jogador = int(input('Diga um valor: '))
    par_impar = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    computador = randint(1, 2)
    soma = jogador + computador
    print('-' * 40)
    if soma % 2 == 0:
        resultado = 'P'
        msg = 'PAR'
    else:
        resultado = 'I'
        msg = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} - DEU {msg}')
    print('-' * 40)
    if par_impar == resultado:
        print('Você VENCEU! \nVamos jogar novamente...\n', '=-' * 20)
        contador += 1
    else:
        print(f'GAME OVER! Você venceu {contador} vezes.')
        break

# ----------------------------------------------------------------------------------------------

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')