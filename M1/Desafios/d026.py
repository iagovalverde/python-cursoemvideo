# PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING
# Faca um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A"
# -> Em que posicao ela aparece a primeira vez
# -> Em que posicao ela aparece a ultima vez

frase = input('Digite uma frase: ')
frase_minuscula = frase.lower()
letra_a = frase_minuscula.count('a')

primeiro_a = frase_minuscula.find('a')

ultimo_a = frase_minuscula.rfind('a')


print(f'A letra "a" aparece {letra_a} vezes')
print(f'A letra "a" aparece a primeira vez na posicao {primeiro_a}')
print(f'O ultimo "a" aparece a ultima vez na posicao {ultimo_a}')