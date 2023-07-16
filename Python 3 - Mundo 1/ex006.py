cores = {'limpa': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'blue': '\033[33m'}

N = int(input('Digite um Valor para saber seu (Triplo), (Dobro), (RaizQ): '))
triplo = N * 3
dobro = N * 2
raiz = N ** (1/2)
print('O Valor digitado foi {}, seu (Triplo) {}{}{}, (Dobro) {}{}{}, (RaizQ) {}{}{}.'.format(N, cores['red'], triplo, cores['limpa'], cores['blue'], dobro, cores['limpa'], cores['green'], raiz, cores['limpa']))