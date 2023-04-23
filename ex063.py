'''
Escreva um programa que leia um numero n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma sequencia de fibonacci.
sequencia de fibonacci: 0 1 1 2 3 5 8
'''
f1 = int(input('Sequencia fibonacci: '))
f2 = f1 + 1
cont = 3
while cont != 0:
    f3 = f1 + f2
    print(f1, f2, f3, end=' ')
    f1 = f2 + f3
    f2 = f3 + f1
    cont -= 1