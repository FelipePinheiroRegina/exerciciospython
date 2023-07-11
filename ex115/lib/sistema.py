from interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('OPÇÃO 1')
    elif resposta == 2:
        cabeçalho('OPÇÃO 2')
    elif resposta == 3:
        cabeçalho('\033[4;31mSAINDO DO SISTEMA... ATÉ LOGO!\033[m')
        sleep(2)
        break
    else:
        print('\033[31m[ ERRO ], Digite uma opção válida!\033[m')
    sleep(2)


