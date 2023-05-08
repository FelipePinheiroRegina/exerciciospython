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
posiçãom = 0
posiçãor = 0
for cont in range(1, 5 + 1):
    Valores.append(int(input(f'Entre com o {cont}° Valor: ')))  # Pedindo para o usuário entrar com 5 valores
for p, v in enumerate(Valores):  # Analisando
    if p == 0:
        Maior = Valores[p]
        Menor = Valores[p]
    if Valores[p] > Maior:
        Maior = Valores[p]
        posiçãom = p
    if Valores[p] < Menor:
        Menor = Valores[p]
        posiçãor = p
print(f'A Lista digitada foi: {Valores}')
print(f'O maior valor digitado foi {Maior} na posição {posiçãom}!')
print(f'O menor valor digitado foi {Menor} na posição {posiçãor}!')

