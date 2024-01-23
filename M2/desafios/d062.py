# SUPER PROGRESSAO ARITMETICA v3.0
# Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.


termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razao da PA: '))
contador = 1
segue_contador = 0
while contador <= 10:
    print(termo, end=' ')
    termo += razao
    contador += 1
print('PAUSA')
resposta = int(input('Quer mostrar mais quantos termos: '))
while resposta > 0:
    while segue_contador < resposta:
        print(termo, end=' ')
        termo += razao
        segue_contador += 1
    print('PAUSA')
    segue_contador = 0
    resposta = int(input('Quer mostrar mais quantos termos: '))


# ---------------------------------------------------------------


print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(termo, end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Progressao finalizada com {total} termos mostrados.')