'''
Crie um programa que simule o funcionamento de um caixa eletronico
No inicio, pergunte ao usuario qual será o valor a ser sacado
(numero inteiro) e o programa vai informar quantas cedulas de cada
valor será entregue
OBS:
 considere que o caixa possui cédulas de 50 20 10 1
'''
print('\033[32m='*25)
print('$$$ BANCO DO LIPIN $$$')
print('='*25, '\033[m')
print('Cédulas |\033[32mR$\033[m 50, 20, 10, 1')
saque = int(input('Digite o valor do Saque: '))
ced = 50
contnota = 0
while True:
    if saque >= ced:
        saque -= ced
        contnota += 1
    else:
        if contnota > 0:
            print(f'Vão ser {contnota} Notas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
             ced = 10
        elif ced == 10:
             ced = 1
        contnota = 0
        if saque == 0:
            break






