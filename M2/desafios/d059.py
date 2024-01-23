# CRIANDO UM MENU DE OPCOES
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# Seu programa deverá realizar a operaçao solicitada em cada caso

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
escolha = 0

while escolha != 5:
    print('[1] somar'
    '\n[2] multiplicar'
    '\n[3] maior'
    '\n[4] novos numeros'
    '\n[5] sair do programa'
    '\n')
    escolha = int(input('Qual sua escolha? '))

    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif escolha == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicacao entre {n1} e {n2} é {multiplicacao}')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior numero é o {maior}')
    elif escolha == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
    print('-' * 10)
