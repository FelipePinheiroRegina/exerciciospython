'''
Faça um programa que leia 5 valores
numéricos e gurade os em uma lista.

no final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições
na lista.
'''
Valores = list()
Maior = 0
Menor = 0
for cont in range(1, 5 + 1):
    Valores.append(int(input(f'Entre com o {cont}° Valor: ')))  # Pedindo para o usuário entrar com 5 valores

for p, v in enumerate(Valores):  # Analisando
