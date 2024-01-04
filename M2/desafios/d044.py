# GERENCIADOR DE PAGAMENTOS
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento: 
# - a vista dinheiro/cheque: 10% desconto
# - a vista no cartao: 5% de desconto
# - em ate 2x no cartao: preco normal
# - 3x ou mais no cartao: 20% de juros

preco = float(input('Valor do produto: '))

pagamento = int(input('Qual o tipo de pagamento? '
                '\n1 - A vista[dinheiro]'
                '\n2 - A vista[cartao]'
                '\n3 - 2x[cartao]'
                '\n4 - 3x ou mais[cartao]'
                '\n'))

if pagamento == 1:
    desconto = preco * 0.9
elif pagamento == 2:
    desconto = preco * 0.95
elif pagamento == 3:
    desconto = preco
elif pagamento == 4:
    desconto = preco * 1.2

print(f'O produto que custa: R${preco} passará a custar R${desconto}')