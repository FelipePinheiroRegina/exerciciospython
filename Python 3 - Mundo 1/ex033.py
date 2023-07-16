''' faça um programa que leia três números, e mostre qual é maior, e qual é o menor
usando estruturas condicionais'''
print('\033[1;32m------'*10)
print('JOGO: QUAL É O MAIOR : QUAL É O MENOR')
print('------'*10)
n1 = int(input('1° número: '))
n2 = int(input('2° número: '))
n3 = int(input('3° número: '))
maior = 0
menor = 0

'''Maior número'''

if n1 > n2 and n1 > n3:
    maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

'''Menor número'''

if n1 < n2 and n1 < n3:
    menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

print('O Maior número: {}'.format(maior))
print('O Menor número: {}'.format(menor))