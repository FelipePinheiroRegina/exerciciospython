'''
faca um programa que leia o ano de nascimento
de um jovem e informe de acordo com sua idade

- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se ja passou do tempo de alistamento

seu programa tambem devera mostrar o tempo que
que falta ou passou do prazo
'''

# forma como eu elaborei o exercicio
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

'''

# Forma como meu professor elaborou
from datetime import date
atual = date.today().year
nascimento = int(input('Qual seu ano de nascimento: '))
idade = atual - nascimento

print('\033[1;34m Quem nasceu em {}, tem {} anos, em {}. \033[m'.format(nascimento, idade, atual))
print('''\033[1;31m IDADE DE ALISTAMENTO NO SERVIÇO MILITAR 
            [ 18 ANOS ] \033[m ''')

if idade == 18:
    print('\033[1;32m Você deve se alistar IMEDIATAMENTE! \033[m'.format(idade))
elif idade < 18:
    sobra = 18 - idade
    print('Ainda faltam \033[1;31m{} anos\033[m, para o seu alistamento.'.format(sobra))
    alist = atual + sobra
    print('Você deverá se alistar em \033[1;32m{}\033[m, pois terá completado a Maioridade!'.format(alist))
elif idade > 18:
    sobra = idade - 18
    print('Você ja deveria ter se alistado, há \033[1;31m{} anos\033[m'.format(sobra))
    alist = atual - sobra
    print('O ano de seu alistamento foi em \033[1;32m{}.\033[m'.format(alist))

