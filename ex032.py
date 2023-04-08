'''Faça um programa que diga se o ano é bissexto ou não'''
'''print('---'*10)
print('O ano é BISSEXTO?')
print('---'*10)
ano = int(input('Em que ano estamos?: '))
fev = int(input('Quantos dias tem o mês de "FEV" no ano de {}?: '.format(ano)))
print('---'*20)
if fev == 29:
    print('O Ano de {}, Tem 366 dias.\nSendo assim ele é um ano BISSEXTO.'.format(ano))
else:
    print('O Ano de {}, Tem 365 dias.\nSendo assim ele Não é um ano BISSEXTO.'.format(ano))'''
from datetime import date
ano = int(input('\033[1;31;40mque ano quer analisar? se colocar o 0, vou considerar ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}, é bissexto!'.format(ano))
else:
    print('O ano de {}, não é bissexto!'.format(ano))
