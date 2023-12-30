# SENO, COSSENO E TANGENTE
# Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians

angulo = float(input('Digite um angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O angulo {angulo}° possui seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}')