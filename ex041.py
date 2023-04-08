'''
a confederação nacional de natação precisa
de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria de acordo
com a idade

  CRITERIOS
  - ate 9 anos == mirim
  - ate 14 ano == infantil
  - ate 19 anos == junior
  - ate 25 anos == senior
  - acima == master
'''
# Meu codigo
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
'''

# Código do professor
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc

print('Idade do Atleta: \033[1;34m{} anos\033[m.'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Senior')
else:
    print('Classificação: Master')