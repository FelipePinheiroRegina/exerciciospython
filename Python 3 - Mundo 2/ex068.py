'''
Faça um programa que joge par ou impar com o computador o jogo só
 será interrompido quando o jogador perder, mostrando o total de vitórias
 consecutivas que ele conquistou no final do jogo
'''
from random import randint
print('=-='*15)
print('{:^45}'.format('PAR OU ÍMPAR'))
print('=-='*15)
totv = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um Valor: '))
    PouI = str(input('Par ou Ímpar: [P/I] ')).upper().strip()[0]
    print(f'O computador jogou o número {computador}')
    resultado = jogador + computador
    print(f'{jogador} + {computador} = {resultado}')
    if resultado % 2 == 0 and PouI == 'P':
        print('Jogador Venceu!')
        totv = totv + 1
    elif resultado % 2 == 1 and PouI == 'I':
        print('Jogador Venceu!')
        totv = totv + 1
    else:
        print('Jogador Perdeu!')
        break
    print('=-='*20)
print(f'Jogador teve {totv} vitórias consecutivas.')
