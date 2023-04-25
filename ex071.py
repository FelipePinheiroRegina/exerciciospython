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
Saque = int(input('Valor do Saque: '))
total = Saque
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
       if totalcéd > 0:
           print(f'Vai ser {totalcéd} de {céd}')
       if céd == 50:
           céd = 20
       elif céd == 20:
           céd = 10
       elif céd == 10:
           céd = 1
       totalcéd = 0
       if total == 0:
           break




