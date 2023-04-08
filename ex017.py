'''co = float(input('Digte o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Cateto oposto {}, Cateto adjacente {}, sua hipotenusa vai ser {:.2f}.'.format(co, ca , hi))'''
from math import hypot

co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hi = hypot(co, ca)
print('\033[1;43m O C.O é {}, o C.A é {}, sua Hipotenusa é {:.2f}'.format(co, ca, hi))