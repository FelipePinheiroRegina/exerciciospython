# Critérios
'''
elabore um jogo que faca o computador jogar
jokenpô com você

    CRITERIOS
- Pedra, papel, tesoura
'''

# Meu código de JokenPO
'''
from random import choice
po1 = 'pedra'
po2 = 'papel'
po3 = 'tesoura'
lista = [po1, po2, po3]
comp = choice(lista)
jogador = input('Pedra, Papel ou Tesoura? ').strip().lower()

if comp == jogador:
    print('Computador escolheu {}'.format(comp.capitalize()))
    print('Jogador escolheu {}'.format(jogador.capitalize()))
    print('IMPATEEEE!')
elif comp == 'papel' and jogador == 'pedra':
    print('Computador escolheu {}'.format(comp.capitalize()))
    print('Jogador escolheu {}'.format(jogador.capitalize()))
    print('Papel embrulha Pedra!')
    print('Computador K.O!')
elif jogador == 'papel' and comp == 'pedra':
    print('Jogador escolheu {}'.format(jogador.capitalize()))
    print('Computador escolheu {}'.format(comp.capitalize()))
    print('Papel embrulha Pedra!')
    print('Jogador K.O!')
elif comp == 'tesoura' and jogador == 'papel':
    print('Computador escolheu {}'.format(comp.capitalize()))
    print('Jogador escolheu {}'.format(jogador.capitalize()))
    print('Tesoura corta Papel!')
    print('Computador K.O!')
elif jogador == 'tesoura' and comp == 'papel':
    print('Jogador escolheu {}'.format(jogador.capitalize()))
    print('Computador escolheu {}'.format(comp.capitalize()))
    print('Tesoura corta Papel!')
    print('Jogador K.O!')
elif comp == 'pedra' and jogador == 'tesoura':
    print('Computador escolheu {}'.format(comp.capitalize()))
    print('Jogador escolheu {}'.format(jogador.capitalize()))
    print('Pedra quebra Tesoura!')
    print('Computador K.O!')
elif jogador == 'pedra' and comp == 'tesoura':
    print('Jogador escolheu {}'.format(jogador.capitalize()))
    print('Computador escolheu {}'.format(comp.capitalize()))
    print('Pedra quebra Tesoura!')
    print('Jogador K.O!')
'''

# Código do Professor Guanabis

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[4;36m{:=^20}\033[m'.format(' JOKENPO '))
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Qual sua escolha? '))
print('JOOOO')
sleep(1)
print('KEEENN')
sleep(1)
print('PÔ!')
print('\033[1;31m=-\033[m'*15)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('\033[1;31m=-\033[m'*15)

if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('IMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA, TENTE NOVAMENTE!')
elif computador == 1: # Computador jogou Papel
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('IMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCEU!')
        else:
            print('JOGADA INVALIDA, TENTE NOVAMENTE!')
elif computador == 2: # Computador jogou Tesoura
        if jogador == 0:
            print('JOGADOR VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('IMPATE!')
        else:
            print('JOGADA INVALIDA, TENTE NOVAMENTE!')