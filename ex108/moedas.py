def aumento(preço, taxa):
    resposta = preço + (preço * taxa / 100)
    return resposta


def diminui(preço, taxa):
    resposta = preço - (preço * taxa / 100)
    return resposta


def metade(preço):
    resposta = preço / 2
    return resposta


def dobro(preço):
    resposta = preço * 2
    return resposta


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')






