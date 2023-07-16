def aumento(preço=0, taxa=0, formato=False):
    resposta = preço + (preço * taxa / 100)
    return resposta if not formato else moeda(resposta)


def diminui(preço=0, taxa=0, formato=False):
    resposta = preço - (preço * taxa / 100)
    return resposta if not formato else moeda(resposta)



def metade(preço=0, formato=False):
    resposta = preço / 2
    return resposta if not formato else moeda(resposta)


def dobro(preço=0, formato=False):
    resposta = preço * 2
    return resposta if not formato else moeda(resposta)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa_A=10, taxa_R=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{moeda(dobro(preço))}')
    print(f'Metade do preço: \t{moeda(metade(preço))}')
    print(f'{taxa_A}% de aumento: \t{moeda(aumento(preço, taxa_A))}')
    print(f'{taxa_R}% de redução:  \t{moeda(diminui(preço, taxa_R))}')








