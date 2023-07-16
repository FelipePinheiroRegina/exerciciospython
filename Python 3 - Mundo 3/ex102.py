def fatorial(num=1, show=False):
    '''
    ==> Calcula o Fatorial de um número.
    :param num: O número a ser fatorado.
    :param show: (OPCIONAL) Mostra a conta de for verdadeiro.
    :return: Retorna o resultado no número.
    '''
    f = 1
    for c in range(num, 0, - 1):
        f *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return f


print(fatorial(5, show=True))
