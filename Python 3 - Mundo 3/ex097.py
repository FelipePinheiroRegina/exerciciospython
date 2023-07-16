'''def printaFrase(f, c):
    print('~' * c)
    print(f'{f}')
    print('~' * c)


frase = str(input('Digite um texto: '))
comp = len(frase) + 1
printaFrase(frase, comp)'''


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Felipe Pinheiro')
