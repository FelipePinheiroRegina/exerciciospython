preco = float(input('\033[35;47mQual é o Preço do Produto: \033[m'))
precod = preco * 5 / 100
print('\033[1;33;40mO preço do produto é {:.2f}, com 5% de desconto ele passará a valer {:.2f}.\033[m'.format(preco, preco - precod))
