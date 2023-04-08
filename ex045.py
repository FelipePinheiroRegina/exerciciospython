'''
elabore um jogo que faca o computador jogar
jokenpô com você

    CRITERIOS
- Pedra, papel, tesoura
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


