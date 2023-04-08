'''
faca um programa que leia o ano de nascimento
de um jovem e informe de acordo com sua idade

- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se ja passou do tempo de alistamento

seu programa tambem devera mostrar o tempo que
que falta ou passou do prazo
'''
from datetime import date
anoatual = date.today().year
nascimento = int(input('Data de Nascimento: '))
idade = anoatual - nascimento

if idade < 16:
    print('Você tem {} anos, está muito novo para se alistar no serviço militar!'.format(idade))
elif idade == 17:
    print('Você tem {} anos, está na idade para se alistar no serviço militar!'.format(idade))
elif idade >= 18:
    print('Você tem {} anos, Já passou do tempo de alistamento no serviço militar!'.format(idade))

