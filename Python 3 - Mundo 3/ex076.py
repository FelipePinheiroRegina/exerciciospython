'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequencia

no final, mostre uma listagem de preços organizando os dados
em forma tabular
'''
Produtos = ('Caneta', 1.99,
            'Lápis', 0.99,
            'Apontador', 1.50,
            'Borracha', 0.50,
            'Mochila', 250,
            'Estoujo', 4.99,
            'Patinete', 500,
            'Coxinha', 3.50,
            'Paçoca', 1)

print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for c in range(0, len(Produtos)):
    if c % 2 == 0:
        print(f'{Produtos[c]:.<30}', end='')
    else:
        print(f'R$ {Produtos[c]:>7.2f}')
print('-' * 40)

#for c in range(0, len(Produtos), 2):    Meu jeito
#    print('{:.<25}{}{:>6.2f}'.format(Produtos[c], 'R$ ', Produtos[c + 1]))
