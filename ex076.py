'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequencia

no final, mostre uma listagem de preços organizando os dados
em forma tabular
'''
Produtos = ('Caneta', 1.99, 'Lápis', 0.99, 'Apontador', 1.50, 'Borracha', 0.50, 'Mochila', 250, 'Estoujo', 4.99, 'Patinete', 500, 'Coxinha', 3.50, 'Paçoca', 1)
print('-' * 30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-' * 30)
for c in range(0, len(Produtos), 2):
    print('{:.<25}{}{:>4.2f}'.format(Produtos[c], 'R$ ', Produtos[c + 1]))
