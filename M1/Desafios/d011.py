# PINTANDO PAREDES
# Faca um programa que leia a largura e a altura de uma parede em metros, calcule  sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura * altura
tinta = area / 2

print(f'A parede de {area}m² necessita de {tinta}L de tinta')