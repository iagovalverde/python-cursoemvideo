# CORES NO TERMINAL
# ANSI - escape sequence
# \033[style; text; back  m
# \033[0;33;44m

#   style         text      back
#                  30        40     white
#   0 None         31        41     red       
#   1 Bold         32        42     green
#   4 Underline    33        43     yellow
#   7 Negative     34        44     darkblue
#                  35        45     purple
#                  36        46     lightblue
#                  37        47     gray

# Padrao
# \033[m

# Inverso
# \033[7;30m

nome = 'Iago'
print('\033[4;37;45mOlá, mundo!')
print('-------------------')
print(f'\033[1;34;47mBem vindo, Iago!\033[m')