'''
Escreva um programa que leia um número inteiro
qualquer e peça para o usuario escolher qual será
a base da conversão:
1 - para binario
2 - para octal
3 - para hexadecimal
'''
''' 
num = int(input('Digite um número: '))
print('\033[1;34m Converter para | Binário / Hexadecimal / octal | \033[m')
converter = str(input(': ')).lower().strip()

binario = bin(num)[2:]
hexa = hex(num)[2:]
octa = oct(num)[2:]

if converter in 'binario binário':
    print('O valor {}, convertido para Binário é "\033[1;31m{}\033[m"'.format(num, binario))
elif converter == 'hexadecimal':
    print('O valor {}, convertido para Hexadecimal é "\033[1;31m{}\033[m"'.format(num, hexa))
elif converter == 'octal':
    print('O valor {}, convertido para Octal é "\033[1;31m{}\033[m"'.format(num, octa))
else:
    print('\033[4;31m [ERRO] REVEJA O CONVERSOR DIGITADO E TENTE NOVAMENTE! \033[m')
'''
num = int(input('Digite um número: '))
opçao = int(input('''Conversões:
[ 1 ] para Binário
[ 2 ] para Hexadecimal
[ 3 ] para Octal
Opção: '''))
if opçao == 1:
    print('O valor {}, convertido para Binário é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O valor {}, convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
elif opçao == 3:
    print('O valor {}, convertido para Octal é {}'.format(num, oct(num)[2:]))
else:
    print('Número Invalido, tente novamente!')



