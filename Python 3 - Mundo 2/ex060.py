'''
Faça um programa que leia um número
qaulquer e mostre o seu fatorial.
ex:
5! = 5x4x3x2x1 = 120
'''
#Meu código
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

print(' = {}'.format(fatorial1))'''

#código do meu professor
'''existe um modo de calcular o fatorail de um número, super facil, que é usando a biblioteca (math)
mas vamos fazer no manual, utilizando a matematica
'''
n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))




