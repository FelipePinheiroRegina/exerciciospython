'''
Crie um programa que leia vários números inteiros pelo teclado
, o programa só vai parar quando o usuario digitar o valor 999
, que é a condição de parada, no final mostre quantos números
foram digitados e qual foi a soma entre eles desconsiderando o
#flag
'''
totnúmeros = soma = 0
while True:
    número = int(input('Digite um número, [ 999 parar ]: '))
    if número == 999:
        break
    totnúmeros += 1
    soma += número
print(f'Você digitou {totnúmeros} números e a soma entre eles é {soma}')
