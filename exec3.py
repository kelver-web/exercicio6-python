# 3. Nome na vertical. Faça um programa que solicite o nome do usuário
# e imprima-o na vertical.

'''
F
U
L
A
N
O
'''

print(' === NOME NA VERTICAL ===')
nome = str(input('Digite o seu nome:  ')).upper()
for i in nome:
    print(f'{i}')