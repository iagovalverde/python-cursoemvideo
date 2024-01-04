# ALISTAMENTO MILITAR
# Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao servico militar.
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento

# Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Digite a idade: '))

if idade < 18:
    print('Ainda vai se alistar.')
elif idade == 18:
    print('Já é a hora de se alistar.')
else:
    print('Já passou do tempo do alistamento')