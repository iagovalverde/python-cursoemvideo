# DETECTOR DE PALINDROMO
# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espacos. Ex: bob | apos a sopa | a sacada da casa

frase = input('Digite uma frase: ').lower().strip().split()
frase_sem_espacos = ''.join(frase)

if frase_sem_espacos == frase_sem_espacos[::-1]:
    print(f'A frase | {frase_sem_espacos} | É um palindromo')
else:
    print(f'A frase | {frase_sem_espacos} | NAO é um palindromo')