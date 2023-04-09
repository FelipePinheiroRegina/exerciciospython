'''
desenvolva uma lógica que leia o
peso e a altura de uma pessoa, caucule seu IMC
e mostre seu status, de acordo com
a tabela abaixo

- abaixo de 18.5 == abaixo do peso
- entre 18.5 e 25 == peso ideal
- acima de 25 ate 30 == sobre peso
- 30 até 40 == obesidade
- acima de 40 == obesidade morbida
'''
from math import sqrt
peso = float(input('Informe seu peso: {Kg} '))
altura = float(input('Informe sua altura: {m} '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do PESO normal')
elif imc <= 25:
    print('PARABÉNS, Você está na faixa de PESO normal')
elif imc <=30:
    print('Você está em SOBREPESO')
elif imc <= 39:
    print('Você está em OBESIDADE, CUIDADO!')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA!, Procure um médico')

