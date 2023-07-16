dias = int(input('\033[1;33m Dias alugados?: \033[m'))
km = float(input('\033[1;33m Km rodados?: \033[m'))
ppdias = dias * 60
ppkm = km * 0.15
print('\033[1;31mVocê alugou o Carro por {} Dias. \nVocê rodou {} Km. \nPreços| 60R$ por dia | 0.15R$ por Km| \nPreço Total à pagar: {:.2f}'.format(dias, km, ppdias + ppkm))