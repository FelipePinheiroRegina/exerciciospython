'''Pergunte ao usuario, quantos km é a viagem dele, e cobre 0.50 $ para viagens
até 200km, para viagens mais longas cobre 0.45 $'''
print('\033[1;33m ---'*20)
print('VALORES DAS PASSAGENS')
print('---'*20)
print('Para Viagens até 200 KM: $ 0.50 por Km')
print('Para Viagens acima disso: $ 0.45 por KM')
print('---'*20)
viagem = int(input('Quantos KM sua Viagem?: '))
if viagem <= 200:
    print('Você vai percorrer: {} KM\nPreço da Passagem: R${:.2f}'.format(viagem, viagem * 0.50))
else:
    print('Você vai percorrer: {} KM\nPreço da Passagem: R${:.2f}'.format(viagem, viagem * 0.45))