'''
Crie um programa que leia vários números inteiros
pelo teclado. o programa só vai parar quando o
usuário digitar o valor 999, que é a condição da para
. no final, mostre quantos números foram digitados e qual foi a soma
entre eles, desconsiderando o flag(o 999)
'''
#Meu Código
'''print('Parar: 999')
cont = 0
totn = 0
c = 0
while c != 999:
    condição = int(input('Digite um número: '))
    if condição != 999:
        cont += condição
        totn += 1
    if condição == 999:
        c = 999
print('Total de valores digitados {}, a soma entre eles é {}.'.format(totn, cont))'''

#Código Professor
soma = cont = 0
núm = int(input('Digite um número: [Parar Digite 999] '))
while núm != 999:
    cont = cont + 1
    soma = soma + núm
    núm = int(input('Digite um número: [Parar Digite 999] '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))