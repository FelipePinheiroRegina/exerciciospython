'''Para salários acima de 1250 = 10% aumento
Para salários menor ou igual 1250 = 15% aumento'''

print('---'*10)
print('  '*5,'HOLERITE')
print('---'*10)
salario = float(input('Salário R$: '))
if salario > 1250:
    salario += salario * 10 / 100
    print('Aumentamos seu salário em 10%, R$ \033[1;32m{:.2f}\033[m'.format(salario))
else:
    salario += salario * 15 / 100
    print('Aumentamos seu salário em 15%, R$ \033[1;32m{:.2f}\033[m'.format(salario))