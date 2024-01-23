# INTERROMPENDO REPETIÇOES WHILE
# break (comando que interrompe loop infinito)

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
