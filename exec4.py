# 4. Nome na vertical em escada. Modifique o programa anterior
# de forma a mostrar o nome em formato de escada.

'''
F
FU
FUL
FULA
FULAN
FULANO
'''

nome = str(input('Digite o seu nome:  '))
escada = ' '

for i in nome:
    escada += i
    print(escada)
