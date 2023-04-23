'''
Faça um programa que leia um número
qaulquer e mostre o seu fatorial.
ex:
5! = 5x4x3x2x1 = 120
'''
fat = int(input('Fatorial: '))
fatorial1 = fat
fatorial = 0
cont = fat - 1
while cont != 0:
    if cont == fat - 1:
        print('{}! = {}'.format(fat, fat), end='')
    print('x{}'.format(cont), end='')
    fatorial = fatorial1 * cont
    fatorial1 = fatorial
    cont = cont - 1

print(' = {}'.format(fatorial1))




