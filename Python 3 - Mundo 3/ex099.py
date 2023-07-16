from random import randint
from time import sleep


def maior(* valores):
    m = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    sleep(1)
    for num in valores:
        print(num, end=' ')
        if num > m:
            m = num
    print(f'Foram analisados {len(valores)} valores ao todo.')
    print(f'O Maior valor informado foi {m}.')


# Programa principal
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior(1, 6, 3)
maior(1, 2)
maior(300, 500, 700, 250, 100, 1000)
maior()
