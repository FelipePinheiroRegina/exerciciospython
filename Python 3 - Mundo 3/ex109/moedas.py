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








