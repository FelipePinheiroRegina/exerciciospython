salario = float(input('Quanto você recebe?: '))
aumento = salario * 15 / 100
print('\033[4;34;40mSeu salário atual é de {:.2f}, você ganha muito pouco!, te darei 15% de aumento salárial. \nVocê passará a ganhar {:.2f}.'.format(salario, salario + aumento))