"""Crie um programa que leia o ano de nascimento
de sete pessoas, no final, mostre qauntas
pessoas aindanão atingiram a maioridade e
quantas ja são maiores"""
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Data de nascimento: '))
    idade = ano - nasc
    if idade > 18:
        maior += 1
    else:
        menor += 1
print('Das datas de nascimento informadas, constatamos que {} são de Maior, e {} são de Menor.'.format(maior, menor))
