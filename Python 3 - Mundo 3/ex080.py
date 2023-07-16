'''
Crie um programa onde o usuário possa
digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção
sem usar o sort().
no final, mostre a lista ordenada na tela.
'''
lista = list()
for contador in range(5):
    n = int(input('Digite um valor: '))
    if contador == 0 or n > lista[- 1]:
        lista.append(n)
        print('Valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print(lista)