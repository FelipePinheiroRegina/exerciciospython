'''faça um programa que calcule a soma entre todos os
numeros impares que são multiplos de tres e que se
encontram no intervalo de 1 ate 500'''

# Resposta
soma = 0
for c in range(1, 502):
    if c % 3 == 0 and c % 2 == 1:
        soma += c
print('A soma de todos os valores ÍMPARES MULTIPLOS de [ 3 ]\nque se encontra no intervalo de (1 até 500) é {}'.format(soma))

