# MANIPULANDO TEXTO

# Fatiamento --------------------------

# C U R S O   E M   V  I  D  E  O     P  Y  T  H  O  N
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#                                       -5 -4 -3 -2 -1

# frase[9:14]   -> VIDEO
# frase[9:21]   -> VIDEO PYTHON
# frase[9:21:2] -> VDO PTO
# frase[:5]     -> CURSO
# frase[15:]    -> PYTHON
# frase[9::3]   -> VE PH

# Análise --------------------------

frase = 'Curso em Video Python'
len(frase) # 21
frase.count('o') # 3
frase.count('o', 0, 13) # 1 (do 0 ao 12)
frase.find('deo') # 11 (posicao que inicia)
frase.find('Android') # -1 (nao existe)
'Curso' in frase # True (existe)

# Transformacao --------------------------

frase.replace('Python', 'Android') # Curso em Video Android
frase.upper() # CURSO EM VIDEO PYTHON
frase.lower() # curso em video python
frase.capitalize() # Curso em video python
frase.title() # Curso Em Video Python

frase2 = '    Aprenda Python  '
frase2.strip() # 'Aprenda Python' (remove espacos no inicio e fim)
frase2.rstrip() # (remove os espacos na direita)
frase2.lstrip() # (remove os espacos na esquerda)

# Divisao --------------------------

frase.split() # Curso # em # Video # Python (separa por espacos e cria uma lista com os itens)

# Juncao --------------------------

'-'.join(frase) # Curso-em-Video-Python

# ---------------------------------

print("""Welcome! Are you completely new to programming? Learn why and how to get started with Python. Fortunately an experienced programmer in any programming language can pick up Python very quickly.""")

1834