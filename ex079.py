'''
Crie um programa onde o usuário possa
digitar vários valores numéricos e cadastre-os
em uma lista, Caso o número já exista la
dentro, ele não será adicionado,
no final, serão exibidos todos os valores
únicos digitados em ordem crescente
'''
Valores = list()
R = ''
while True:
    Valores.append(int(input('Digite um valor: ')))
    for v in Valores:
        if v == Valores:
            print('Valor Repetido!, Digite novamente!')
            Valores.append(int(input('Digite outro valor: ')))
        else:
            print('Valor Registrado!')
    R = str(input('Quer continuar? [ S / N ]: '))
    if R in 'Nn':
        break


