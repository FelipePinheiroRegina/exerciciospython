'''refaça o desafio 009, mostrando
a tabuada de um número que o usuario
escolher, só que agora utilizando um laço for'''
n = int(input('Tabuada: '))
for c in range(1, 10 + 1):
    print('\033[4;34m{} x {:>2} = {:>2}\033[m'.format(n, c, n * c))