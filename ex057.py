'''
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F.
caso esteja errado, peça a digitação
novamente até ter um valor correto.
'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('[SEXO INVALIDO, DIGITE NOVAMENTE!]')
print('Sexo[{}].'.format(sexo))