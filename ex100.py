from random import randint
from time import sleep


def sorteio(l):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        n = randint(1, 10)
        l.append(n)
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')
    sleep(1)



def somaPar(l):
    print('\033[31mSOMANDO OS PARES...\033[m')
    sleep(1.4)
    s = 0
    for núm in l:
        if núm % 2 == 0:
            s += núm
    print(f'A soma dos Pares é {s}')


# Programa principal
lista = []
sorteio(lista)
somaPar(lista)
