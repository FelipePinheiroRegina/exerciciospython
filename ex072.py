'''
Desafio 072...
Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso. de zero até vinte.

Seu programa deverá ler um número pelo telcado(ente 0 e 20)
e mostrá-lo por extenso.
'''

Números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
'Doze', 'Teze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    Posição = int(input('Digte um número: (entre 0 e 20) '))
    if Posição >= 0 and Posição <=20:
        print(f'Você digitou o número {Números[Posição]}')
        break

