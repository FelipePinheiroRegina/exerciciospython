'''
a confederação nacional de natação precisa
de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria de acordo
com a idade

  CRITERIOS
  - ate 9 anos == mirim
  - ate 14 ano == infantil
  - ate 19 anos == junior
  - ate 20 anos == senior
  - acima 20 anos == master
'''
from datetime import date
ano = date.today().year

nome = input('Nome do Atleta: ')
nascimento = int(input('Data de Nascimento: '))
idade = ano - nascimento

if idade <= 9:
    print('Nome do Atleta:', nome)
    print('Idade:', idade)
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Nome do Atleta:', nome)
    print('Idade:', idade)
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Nome do Atleta:', nome)
    print('Idade:', idade)
    print('Categoria: JÚNIOR')
elif idade <= 20:
    print('Nome do Atleta:', nome)
    print('Idade:', idade)
    print('Categoria: SENIOR')
else:
    print('Nome do Atleta:', nome)
    print('Idade:', idade)
    print('Categoria: MASTER')