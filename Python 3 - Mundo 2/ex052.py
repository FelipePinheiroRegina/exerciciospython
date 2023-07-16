'''faça um programa que leia um número
inteiro e diga se ele é ou não um número primo'''
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m {}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m {}'.format(c), end=' ')
print('\033[m\nO número {} é divisível por {} números.'.format(num, tot))
if tot == 2:
    print('Por isso ele é PRIMO.')
else:
    print('Por isso ele não é PRIMO.')