# 2. Nome ao contrário em maiúsculas. Faça um programa que permita
# ao usuário digitar o seu nome e em seguida mostre o nome do usuário
# de trás para frente utilizando somente letras maiúsculas. Dica:
# lembre−se que ao informar o nome o usuário pode digitar letra
#  maiúsculas ou minúsculas.


print(' === NOME AO CONTRÁRIO EM MAIÚSCULAS ===')

nome = str(input('Digite o seu nome:  ')).upper()
print(f'{(nome[::-1])}')
