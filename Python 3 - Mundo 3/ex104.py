def LeiaInteiro(num):
    num = input('Digite um número: ')
    while True:
        if num.isnumeric():
            return num
            break
        else:
            print(f'\033[1;31mDigite um número inteiro valido.\033[m')
            num = input('Digite um número: ')


# Programa principal
n = LeiaInteiro('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')