num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[1;31m Unidades: {}'.format(u))
print('\033[1;32m Dezenas: {}'.format(d))
print('\033[1;33m Centenas: {}'.format(c))
print('\033[1;34m Milhas: {}'.format(m))

