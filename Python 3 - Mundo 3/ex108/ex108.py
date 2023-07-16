import moedas

n = float(input('Entre com o preço: R$ '))
print(f'A metade do preço de {moedas.moeda(n)} é {moedas.moeda(moedas.metade(n))}')
print(f'O dobro do preço de {moedas.moeda(n)} é {moedas.moeda((moedas.dobro(n)))}')
print(f'Aumentando 10%, fica {moedas.moeda(moedas.aumento(n, 10))}')
print(f'Diminuindo 10%, fica {moedas.moeda(moedas.diminui(n, 10))}')



