try:
    núm_inteiro = int(input('Entre com um número inteiro: '))
except (TypeError, ValueError):
    while True:
        print(f'ERRO, por favor digite um número inteiro válido!')
        núm_inteiro = str(input('Entre com um número inteiro: ')).strip()
        if núm_inteiro.isnumeric() or núm_inteiro != '':
            núm_inteiro = int
            break
else:
    print(f'O número inteiro foi {núm_inteiro}')


