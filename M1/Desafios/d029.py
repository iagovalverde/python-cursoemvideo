# RADAR ELETRONICO
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual a velocidade do carro? '))
excedente = v - 80
multa = excedente * 7
if (v > 80):
    print('Voce foi multado!'
        f'\nVoce superou a veloc max em {excedente}Km/h.'
        f'\nA multa é de R${multa}')

