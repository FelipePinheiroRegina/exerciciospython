'''
Crie um programa onde o usuário possa
digitar vários valores numéricos e cadastre-os
em uma lista, Caso o número já exista la
dentro, ele não será adicionado,
no final, serão exibidos todos os valores
únicos digitados em ordem crescente
'''
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existente!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
lista.sort()
for v in lista:
    print(f'{v}.. ', end='')



