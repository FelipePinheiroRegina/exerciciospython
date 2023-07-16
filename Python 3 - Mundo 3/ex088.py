'''from random import randint
from time import sleep
principal = []
temp = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
vezes = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-= SORTEANDO {vezes} JOGOS =-=-=')
for c in range(1, vezes + 1):
    for six in range(6):
        temp.append(randint(1, 60))
    principal.append(temp[:])
    temp.clear()
for i, jogo in enumerate(principal):
    sleep(1)
    print(f'Jogo {i + 1}: {jogo}')'''
from random import randint
temp = list()
principal = list()
vezes = int(input('Quantos jogos você quer que eu soteie? '))
tot = 1
while tot <= vezes:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    principal.append(temp[:])
    temp.clear()
    tot += 1
for i, j in enumerate(principal):
    print(f'Jogo {i + 1}: {j}')