import moedas

n = float(input('Entre com o preço: R$ '))
print(f'A metade de {n} é {moedas.metade(n)}')
print(f'O dobro de {n} é {moedas.dobro(n)}')
print(f'Aumentando 10% fica {moedas.porcentagem(n)}')
