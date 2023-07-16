'''
Escreva um programa que leia um numero n inteiro
qualquer e mostre na tela os n primeiros elementos
de uma sequencia de fibonacci.
sequencia de fibonacci: 0 1 1 2 3 5 8
'''
#Meu código
'''cont = int(input('Sequencia fibonacci: '))
f1 = 0
f2 = f1 + 1
while cont != 0:
    f3 = f1 + f2
    print(f1, f2, f3, end=' ')
    f1 = f2 + f3
    f2 = f3 + f1
    cont -= 1
'''

#Código do meu professor
print('---'*10)
print('Sequencia Fibonacci')
print('---'*10)
n = int(input('Quer mostrar quantos termos? '))
print('~~~~'*10)
f1 = 0
f2 = 1
c = 3
print('{} => {} =>'.format(f1, f2), end=' ')
while c <= n:
    f3 = f1 + f2
    print('{} => '.format(f3), end=' ')
    f1 = f2
    f2 = f3
    c += 1
print('FIM')