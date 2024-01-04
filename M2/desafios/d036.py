# APROVANDO EMPRESTIMO
# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Qual o salario do comprador? '))
tempo_pagamento = int(input('Em quanto tempo vai pagar [anos]? '))

pagamento_meses = tempo_pagamento * 12
prestacao = valor_casa / pagamento_meses
valor_max = salario_comprador * 0.3
porcentagem_salario = prestacao / salario_comprador * 100

print(f'Valor da casa: R${valor_casa}'
    f'\nSalario do comprador: R${salario_comprador}'
    f'\nTempo de pagamento: {pagamento_meses} meses'
    f'\nValor da prestacao: R${prestacao:.2f}')
if prestacao < valor_max:
    print(f'Prestacao {porcentagem_salario:.2f}% do salario do comprador'
        '\nEmprestimo APROVADO')
elif prestacao > valor_max:
    print(f'Prestacao {porcentagem_salario:.2f}% do salario do comprador'
        '\nEmprestimo RECUSADO')