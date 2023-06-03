'''
Faça um programa que leia 5 valores
numéricos e gurade os em uma lista.

no final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições
na lista.
'''
valores = []
mai = 0
men = 0
for c in range(5):
    valores.append(int(input(f'Digite o {c + 1}° valor: ')))
    if c == 0:
        mai = men = valores[c]
    if valores[c] > mai:
        mai = valores[c]
    if valores[c] < men:
        men = valores[c]
print(f'VALORES DIGITADOS: {valores}.')
print(f'O maior número digitado foi {mai}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}.. ', end='')
print(f'\nO menor número digitado foi {men}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}.. ', end='')



