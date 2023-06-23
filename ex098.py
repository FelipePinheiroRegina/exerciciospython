from time import sleep

'''
def contador(i, f, p=0):
    print('-=' * 20)
    if i == 1 and f == 10:
        print('Contagem de 1 até 10, de 1 em 1.')
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.5)
        print('Fim!')
    elif i == 10 and f == 0:
        print('Contagem de 10 até 0, de 2 em 2.')
        for c in range(i, f - 2, - 2):
            print(c, end=' ')
            sleep(0.5)
        print('Fim!')
    else:
        print(f'Contagem de {i} até {f}, de {p} em {p}.')
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.5)
        print('Fim!')


contador(1, 10, 1)
contador(10, 0)
print('-=' * 20)
inicio = int(input('Digite um inicio: '))
fim = int(input('Digite um fim: '))
passo = int(input('Digite um passo'))
contador(inicio, fim, passo)
'''


def contador(i, f, p):
    if p < 0:
        p *= - 1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f}, de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Digite um Inicio: '))
fim = int(input('Digite um Fim: '))
passo = int(input('Digite um Passo: '))
contador(inicio, fim, passo)


