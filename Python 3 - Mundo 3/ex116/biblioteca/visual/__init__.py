def LeiaInt(Verificar):
    while True:
        try:
            resp = int(input(Verificar))
        except (ValueError, TypeError):
            print('\033[31mERRO, Por favor, entre com um número inteiro.\033[m')
            continue
        else:
            return resp

def linha(tam=40):
    return '-' * tam
def cabeçalho(msg):
    print(linha())
    print(f'{msg}'.center(40))
    print(linha())


def menu(lista):
    cont = 1
    for opção in lista:
        print(f'\033[1;33m{cont}\033[m - \033[1;34m{opção}\033[m')
        cont += 1
    print(linha())
    opc = LeiaInt('\033[1;33mOPÇÃO:\033[m ')
    return opc

