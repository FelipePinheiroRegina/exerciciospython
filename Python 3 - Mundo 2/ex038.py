'''
Escreva um programa que leia dois numeros
inteiros e compare-os mostrando na tela
uma mensagem:
 - o primeiro valor é maior
 - o segundo valor é maior
 - nao existe valor maior os dois são iguais
'''
from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('\033[1;31m COMPARANDO OS NÚMEROS... \033[m')
sleep(3)
if n1 > n2:
    print('\033[1;36m O primeiro valor é MAIOR \033[m')
elif n2 > n1:
    print('\033[1;35m O segundo valor é MAIOR \033[m')
else:
    print('\033[1;32m Os dois valores são IGUAIS \033[m')