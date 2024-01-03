# AUMENTOS MULTIPLOS
# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Salario do funcionario: '))
if (salario > 1250):
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15
print(f'O salario de R${salario} passará a ser de R${novo_salario:.2f}')