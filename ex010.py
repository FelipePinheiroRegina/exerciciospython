reais = float(input('R$: '))
dolar = reais * 0.19
print('\033[1;42mVocê tem {:.2f} Reais/R$, com esse valor você consegue comprar {:.2f} Dolares/U$.\033[m'.format(reais, dolar))