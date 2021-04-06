# 5. Nome na vertical em escada invertida. Altere o programa anterior
# de modo que a escada seja invertida.
'''
FULANO
FULAN
FULA
FUL
FU
F
'''

nome = input('Digite o seu nome:  ')
invertida1 = ''
invertida2 = ''

for letra in nome:
    invertida1 += letra

for i in range(len(nome)):
    invertida2 = invertida1[0:len(nome) - i]
    print(invertida2)
