'''
Crie um programa que leia dois valores
e mostre um menu na tela:
1 somar
2 multiplicar
3 maior
4 novo números
5 sair do programa
'''
from time import sleep
sair = 0
print('\033[35m=-='*20, '\033[m')
n1 = int(input('Digte um número: '))
n2 = int(input('Digite outro número: '))
while sair != 5:
    print('\033[31mCARREGANDO OPÇÕES...\033[m')
    sleep(1)
    print('\033[34m===='*25, '\033[m ')
    print(('\033[34mOPÇÕES:\033[m [ 1 ] SOMAR \033[34m|\033[m [ 2 ] MULTIPLICAR \033[34m|\033[m [ 3 ] MAIOR \033[34m|\033[m [ 4 ] NOVOS NÚMEROS \033[34m|\033[m [ 5 ] SAIR'))
    opçao = int(input('OPÇÃO: '))
    if opçao == 1:
        print('\033[32mSOMANDO...\033[m')
        sleep(1)
        print('{} + {} = {}.'.format(n1, n2, n1 + n2))
    elif opçao == 2:
        print('\033[36mMULTIPLICANDO...\033[m')
        sleep(1)
        print('{} x {} = {}.'.format(n1, n2, n1 * n2))
    elif opçao == 3:
        print('\033[33mVERIFICANDO O MAIOR...\033[m')
        sleep(1)
        if n1 > n2:
            print('O número {} é maior que {}.'.format(n1, n2))
        else:
            print('O número {} é maior que {}.'.format(n2, n1))
    elif opçao == 4:
        print('\033[36mABRINDO NOVOS NÚMEROS...\033[m')
        sleep(1)
        n1 = int(input('Digte um número: '))
        n2 = int(input('Digite outro número: '))
    elif opçao == 5:
        print('\033[31;40mSAINDO...\033[m')
        sleep(3)
        sair = opçao