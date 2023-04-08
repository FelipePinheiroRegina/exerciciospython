'''from random import choice
lista = [1, 2, 3, 4, 5]
numero = choice(lista)
print('--------Jogo do Chute--------')
print('Tente advinhar qual é o numero escolhido pelo CPU')
numeroU = int(input('Chute o Numero: '))
if numeroU == numero:
    print('Acertou Mizeravi!')
    print('Numero sorteado: {}\nNumero chute: {}'.format(numero, numeroU))
else:
    print('Errou Mizeravi!')
    print('Numero sorteado: {}\nNumero chute: {}'.format(numero, numeroU))'''

from random import randint
from time import sleep
computador = randint(0, 5) # randint faz o computador gerar um número aleatorio
print('\033[1;33m -=- \033[m'*20)
print('\033[35m Vou pensar em um número de 0 a 5, tente advinhar... \033[m')
print('\033[1;33m -=- \033[m'*20)
jogador = int(input('\033[35m Qual número estou pensando?: \033[m'))
print('\033[1;31;40m PROCESSANDO... \033[m')
sleep(1.3)
if jogador == computador:
    print('\033[1;35m VOCÊ CONSEGUIU ME VENCER!')
else:
    print('\033[1;35m EU SOU INEVITÁVEL, PENSEI NO NÚMERO {}, E VOCÊ CHUTOU {}'.format(computador, jogador))
