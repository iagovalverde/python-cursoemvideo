# INDICE DE MASSA CORPORAL
# Desenvolva uma logica que leia o peso e a alura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 ate 30: Sobrepeso
# - 30 ate 40: Obesidade
# - Acima de 40: Obesidade morbida

peso = float(input('Digite o peso [Kg]: '))
altura_cm = float(input('Digite a altura [m]: '))
altura = altura_cm / 100
imc = peso / (altura**2)

print(imc)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')