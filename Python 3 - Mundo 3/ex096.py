print('Controle de Terreno')
print('-' * 20)


def Calc(x, y):
    print(f'A área de um terreno {x} por {y} é de {x * y}m²')


l = float(input('Largura: '))
c = float(input('Comprimento: '))
Calc(l, c)
