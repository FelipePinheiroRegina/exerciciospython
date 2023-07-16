'''
Crie um programa que vai ler vários números
e colocar em uma lista.
Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares
digitados, respectivamente
ao final, mostre o conteúdo ddas três
listas geradas.
'''
lista = []
listaimp = []
listapar = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimp.append(v)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'Todos valores da lista: {lista}')
print(f'Todos valores Pares da lista: {listapar}')
print(f'Todos valores Impares da lista: {listaimp}')
