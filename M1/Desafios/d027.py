# PRIMEIRO E ULTIMO NOME DE UMA PESSOA
# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

n = input('Digite um nome: ')
nomes = n.split()
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f'Primeiro: {primeiro_nome}'
    f'\nÚltimo: {ultimo_nome}')