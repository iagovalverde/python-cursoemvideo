# AQUELE CLASSICO DA MEDIA
# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
# - Media abaixo de 5.0: Reprovado
# - Media entre 5.0 e 6.9: Recuperacao
# - Media 7.0 ou superior: Aprovado

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(media)
if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('Recuperacao')
else:
    print('Aprovado')
