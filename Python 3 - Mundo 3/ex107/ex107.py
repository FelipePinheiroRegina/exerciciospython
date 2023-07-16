import moedas

n = float(input('Entre com o preço: R$ '))
print(f'Aumentando 10% fica R${moedas.aumento(n, 10)}')
print(f'Diminuindo 10% fica R${moedas.diminui(n, 10)}')
print(f'A metade do preço de R${n} fica R${moedas.metade(n)}')
print(f'O dobro do preço de R${n} fica R${moedas.dobro(n)}')

