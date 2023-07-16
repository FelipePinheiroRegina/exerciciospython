from random import shuffle
cor = {'limpa': '\033[m', 'backv': '\033[41m', 'backa': '\033[44m', 'backg': '\033[42m'}
n1 = str(input('{} 1° aluno: {}'.format(cor['backv'], cor['limpa'])))
n2 = str(input('{} 2° aluno: {}'.format(cor['backv'], cor['limpa'])))
n3 = str(input('{} 3° aluno: {}'.format(cor['backa'], cor['limpa'])))
n4 = str(input('{} 4° aluno: {}'.format(cor['backa'], cor['limpa'])))
n5 = str(input('{} 5° aluno: {}'.format(cor['backg'], cor['limpa'])))
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print('\033[1;31m A ordem será: ')
print(lista)