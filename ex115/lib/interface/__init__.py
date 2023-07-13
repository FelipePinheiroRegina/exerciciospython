def LeiaInt(Verificar):
    while True:
        try:
            resp = int(input(Verificar))
        except (ValueError, TypeError):
            print('\033[31mERRO, Por favor, entre com um número inteiro.\033[m')
            continue
        else:
            return resp

def linha(tam=42):
    return '-' * tam


def cabeçalho(msg):
    print(linha())
    print(f'{msg}'.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m[ {c} ] -\033[m \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('\033[1;33mOPÇÃO: \033[m')
    return opc

