'''
Melhore o jogo do desafio 028 onde o computador,
vai 'pensar' em um número entre 0 a 5
só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram
necessário para vencer.
'''
#meu código
'''
from random import randint
computador = 1
jogador = 0
totv = 0
print('\033[32m==='*30, '\033[m')
print('\033[33m COMPUTADOR FALANDO -> "TENTE ADIVINHAR QUE NÚMERO ESTOU PENSANDO, HAHAHA!"')
print('\033[32m==='*30, '\033[m')
while jogador != computador:
    computador = randint(0, 5)
    jogador = int(input('Número: '))
    print('\033[33m COMPUTADOR FALANDO -> "PENSEI NO NÚMERO {}" '.format(computador))
    if jogador != computador:
        print('\033[33m COMPUTADOR FALANDO -> "VOCÊ ERROU HAHA!, TENTE NOVAMENTE!"\033[m')
        totv += 1
print('\033[33m COMPUTADOR FALANDO -> "VOCÊ CONSEGUIU ME VENCER!"')
print(' COMPUTADOR FALANDO -> "MAS PRECISOU DE {} CHANCES! HAHAHA!!!!"\033[m'.format(totv + 1))'''

#código do professor
from random import randint
computador = randint(0, 10)
print('Sou seu computador, Pensei em um número entre 0 e 10.')
print('Será que você consegue adivinhar? ')
palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        else:
            print('Menos... tente mais uma vez')
print('Você acertou, mas precisou de {} tentativas'.format(palpite))


