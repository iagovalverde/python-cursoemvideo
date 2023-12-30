# TIPOS PRIMITIVOS
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
s = n1 + n2
print('A soma vale', s)

# int -> 7 -4 0 987
# float -> 4.5 0.076 1.0
# bool -> True False
# str -> 'ola' 'tudo bem?' '74'  

# SAIDA DE DADOS
# format
print(f'A soma vale {s}')

# metodos da variavel N
n = input('Digite um valor: ')
print(type(n))
print(n.isalnum())
print(n.isnumeric())
print(n.islower())