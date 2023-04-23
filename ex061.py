'''
Refaça o DESAFIO 051, lendo o primeiro
termo e a razão de um P.A, mostrando os 10
primeiros termos daprogressão usando
estrutura while.

Desenvolva um programa que leia o
primeiro termo e a razão de uma PA. no final, mostre
termos dessa progressão
'''

p1 = int(input('Primeiro termo da P.A: '))
razao = int(input('Qual a razão da P.A: '))
cont = 10
while cont != 0:
    if razao > 0:
        print('{}'.format(p1), end=' ')
        p1 += razao
        cont -= 1
    elif razao == 0:
        print('{}'.format(p1), end=' ')
        p1 += razao
        cont -= 1
    elif razao < 0:
        print('{}'.format(p1), end=' ')
        p1 += razao
        cont -= 1
if razao > 0:
    print('\nP.A CRESCENTE!')
elif razao == 0:
    print('\nP.A CONSTANTE!')
elif razao < 0:
    print('\nP.A DECRESCENTE!')