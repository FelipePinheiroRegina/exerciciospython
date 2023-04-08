'''
elabore um programa que calcule o valor a ser
pago por um produto, considerando o seu
preço normal e condição de pagamento

    CRITERIOS
- a vista dinheiro / cheque tem 10% desconto
- a vista no cartão tem 5% de desconto
- em até duas vezes no cartao preço normal
- 3x ou mais no cartao 20% de juros
'''
print('\033[1;34m=================')
print('Eletro Domesticos')
print('=================\033[m')
print('\033[1;31mTV 40 Polegada Ultra LED\033[m')
print('Preço: \033[1;32mR$ 2.000\033[m')
print('\033[1;34m---------------------------------\033[m')
print('\033[1;31mCaixa de SOM JBL\033[m')
print('Preço: \033[1;32mR$ 3.000\033[m')
print('\033[1;34m---------------------------------\033[m')
print('\033[1;31mComputador Gamer\033[m')
print('Preço: \033[1;32mR$ 7.000\033[m')
print('\033[1;34m---------------------------------\033[m')
print('\033[1;31mFORMAS DE PAGAMENTO\033[m')
print('''\033[1;34m
- [dinheiro] ou [cheque] tem 10% desconto
- a vista no [cartão] tem 5% de desconto
- [2x no cartão] preço normal
- 3x ou mais no cartao 20% de juros\033[m
''')
tv = 2.000
som = 3.000
pc = 7.000
pçd = 0
preçoapagar = 0

produto = input('Qual vai ser o produto? ').lower().strip()
if produto in 'tv televisao televisão':
    produto = tv
    print('Que linda TV que você quer comprar!')
elif produto in 'som caixa jbl':
    produto = som
    print('Essa Caixa De Som é muito boa e alta!')
elif produto in 'pc computador pc gamer':
    produto = pc
    print('Esse pc roda todos os jogos em ultra resolução\nótima escolha companheiro!')

pagamento = input('Qual vai ser a forma de pagamento? ').lower().strip()

if pagamento == 'dinheiro' or pagamento == 'cheque':
    pçd = produto * 10 / 100
    preçoapagar = produto - pçd
    print('O preço é R${:.3f}, com 10% de desconto fica R${:.3f}'.format(produto, preçoapagar))
elif pagamento in 'cartao 1x cartão 1x a vista no cartao a vista no cartão 1x no cartao 1x no cartão':
    pçd = produto * 5 / 100
    preçoapagar = produto - pçd
    print('O preço é R${:.3f}, com 5% de desconto fica R${:.3f}'.format(produto, preçoapagar))
elif pagamento in '2x no cartão 2x no cartao':
    print('O preço é R${:.3f}, vai ficar 2x de R${:.3f}'.format(produto, produto / 2))
else:
    pçd = produto * 20 / 100
    preçoapagar = produto + pçd
    print('O preço é {:.3f}, com 20% de juros fica R${:.3f}'.format(produto, preçoapagar))


