'''faça um programa que leia o peso
de cinco pessoas. no final, mostre qual foi
o maior e o menor peso lidos'''
#Meu código
'''maior = 0
menor = 300
for c in range(1, 6):
    Kg = float(input('Digite seu peso: {Kg}'))
    if Kg > maior:
        maior = Kg
    elif Kg < menor:
        menor = Kg
print('O Maior peso informado foi {} Kg, e o Menor peso informado foi {} Kg.'.format(maior, menor))
'''

#Código professor
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))


