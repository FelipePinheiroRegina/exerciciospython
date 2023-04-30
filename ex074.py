'''
Crie um programa que vai gerar cinco números aleatórios e
colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla
'''
from random import randint
n1 = randint(1, 100)
n2 = randint(1, 100)
n3 = randint(1, 100)
n4 = randint(1, 100)
n5 = randint(1, 100)
# Professor n = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100),)
Números = (n1, n2, n3, n4, n5)
for c in Números:
    print('\033[36m', c, end=' \033[m')
print(f'\nO Maior Número é {max(Números)}')
print(f'O Menor Número é {min(Números)}')
