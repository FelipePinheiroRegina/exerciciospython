'''faça um programa que calcule a soma entre todos os
numeros impares que são multiplos de tres e que se
encontram no intervalo de 1 ate 500'''
#Meu código
'''soma = 0
for c in range(1, 502):
    if c % 3 == 0 and c % 2 == 1:
        print(c)
        soma += c
print('A soma de todos os valores ÍMPARES MULTIPLOS de [ 3 ]\nque se encontra no intervalo de (1 até 500) é {}'.format(soma))
'''

#Código do Professor
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma dos {} Valores é {}'.format(cont, soma))

