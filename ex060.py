'''
Faça um programa que leia um número
qaulquer e mostre o seu fatorial.
ex:
5! = 5x4x3x2x1 = 120
'''
fatorail = int(input('Número: '))
fatorail2 = fatorail

while fatorail2 != 0:
    x = fatorail * (fatorail2 - 1)
    fatorail = x

print(fatorail)




