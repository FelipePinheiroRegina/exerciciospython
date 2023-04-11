'''Desenvolva um programa que leia seis
número inteiros e mostre a soma apenas
daqueles que forem pares. se o valor
digitado for ímpar, desconsidere-o'''
somapar = 0
for c in range(1, 6 + 1):
    n = int(input('Número: '))
    if n % 2 == 0:
        somapar += n
print('Somando todos valores pares, deu {}'.format(somapar))