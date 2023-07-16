'''
1 - Pergunte o valor da casa
2 - Pergunte o salario do comprador
3 - Pergunte quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salario ou então
o emprestimos sera negado
'''
from time import sleep

# Perguntas feitas ao comprador
casa = float(input('Qual o valor do Imóvel: '))
salario = float(input('Qual o seu Salário: '))
parcela = int(input('Em quantos anos quer financiar: '))

# Calculos feitos para chegar as respostas
trintsalario = salario * 30 / 100
valormensal = casa / (parcela * 12)

# Sistema de contemplação
print('\033[1;31m PROCESSANDO INFORMAÇÕES... \033[m')
sleep(2)

print('O valor do imóvel é R$ {:.3f}\nDividido em {} anos\nPor mês você pagará R$ {:.3f}'.format(casa, parcela, valormensal))
print('\033[1;34m ANALISANDO COMTEMPLAÇÃO DO EMPRÉSTIMO... \033[m')
sleep(5)
print('30% do seu salário é R$ {:.3f}'.format(trintsalario))
if trintsalario >= valormensal:
    print('Você foi contemplado pois o valor da parcela não excede 30% do seu salário!')
elif trintsalario < valormensal:
    print('Você não foi contemplado pois o valor da parcela excede 30% do seu sálario!')

