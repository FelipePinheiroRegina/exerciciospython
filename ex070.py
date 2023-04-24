'''
Crie um programa que leia o nome e o preço de varios produtos
o programa deverá perguntar se o usuario vai continuar.
no final mostra:
# qual é o total gasto na compra
# quantos produtos custam mais de 1000
# qual é o nome do produto mais barato
'''

print('\033[36m-+-+'*7)
print('|                          |')
print('|    ATACADÃO DO FELIPÃO   |')
print('|                          |')
print('-+-+'*7,'\033[m')
valortotal = qtsmaior1000 = barato = 0
nomebarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    if valortotal == 0:
        barato = preço
        nomebarato = nome
    elif preço < barato:
        barato = preço
        nomebarato = nome
    valortotal = valortotal + preço
    if preço > 1000:
        qtsmaior1000 = qtsmaior1000 + 1
    opçao = str(input('Vai comprar mais produtos - [ S / N ]: ')).strip().upper()[0]
    while not opçao in 'S N':
        print('Opção invalida!')
        opçao = str(input('Vai comprar mais produtos - [ S / N ]: ')).strip().upper()[0]
    if opçao == 'N':
        print('ATÉ BREVE, FIEL CLIENTE!')
        break
print(f'Valor total R$ {valortotal:.2f}.')
print(f'Você comprou {qtsmaior1000} produtos que custam mais que R$ 1.000.')
print(f'Você comprou o produto {nomebarato}, no valor de R$ {barato:.2f}, que é o mais barato entre suas compras.')
