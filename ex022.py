'''print('=========ANALISADOR DE IDADE============')
nome = str(input('Digite seu Nome Completo: '))
dividido = nome.split()
print('Seu Nome é ',nome[0::])
print('Seu Nome em Maiúsculas é {}'.format(nome.upper()))
print('Seu Nome em Minúsculas é {}'.format(nome.lower()))
print('Seu Nome Completo tem {} Letras'.format(len(''.join(dividido))))
print('Seu Primeiro Nome tem {} Letras'.format(len(dividido[0])))'''
from time import sleep
nome = str(input('Nome Completo: ')).strip()
print('\033[1;36m Analisando nome!')
sleep(3)
print('Em Maiúsculas {}'.format(nome.upper()))
print('Em Minúsculas {}'.format((nome.lower())))
print('Seu Nome Completo tem {} Letras'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro Nome tem {} Letras'.format(nome.find(' ')))

