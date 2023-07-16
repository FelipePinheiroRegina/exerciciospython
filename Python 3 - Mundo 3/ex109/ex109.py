import moedas

n = float(input('Entre com o preço: R$ '))
print(f'A metade do preço de {moedas.moeda(n)} é {moedas.metade(n, True)}')
print(f'O dobro do preço de {moedas.moeda(n)} é {moedas.dobro(n, True)}')
print(f'Aumentando em 10%, fica {moedas.aumento(n, 10, True)}')
print(f'Reduzindo em 13%, fica {moedas.diminui(n, 13, True)}')



