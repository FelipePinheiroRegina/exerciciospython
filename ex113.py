def LeiaInt(Verificar):
    while True:
        try:
            resp = int(input(Verificar))
        except (ValueError, TypeError):
            print('\033[31mERRO, Por favor, entre com um número inteiro.\033[m')
            continue
        else:
            return resp


def LeiaFloat(Verificar):
    while True:
        try:
            resp = float(input(Verificar))
        except (ValueError, TypeError):
            print('\033[31mERRO, Por favor, entre com um número real.\033[m')
            continue
        else:
            return resp


núm = LeiaInt('Entre com um inteiro: ')
númf = LeiaFloat('Entre com um real: ')
print(f'Número Inteiro = [  \033[32m{núm}\033[m  ]')
print(f'Número Real = [  \033[36m{númf}\033[m  ]')



