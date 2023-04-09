''' crie um programa que mostre na tela todos
os números pares que estão no intervalo entre 1 e 50'''
for c in range(1, 51):
    if c % 2 == 0:
        print('\033[1;32m', c, end=', \033[m')
