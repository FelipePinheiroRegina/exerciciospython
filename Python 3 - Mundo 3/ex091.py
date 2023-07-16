from random import randint
from operator import itemgetter
from time import sleep
dado = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in dado.items():
        print(f'{k} Tirou {v}.')
        sleep(1)
print('======= RANKING =======')
ranking = list()
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True) #ordena por valor
for i, j in enumerate(ranking):
        print(f'{i + 1}° Lugar: {j[0]} com {j[1]}')
        sleep(1)



