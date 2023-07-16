from interface import *
from arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Mostra as pessoas cadastradas no meu sistema
        lerPessoas(arq)    
    elif resposta == 2:
        # Cadastra uma nova pessoa
        cabeçalho('OPÇÃO 2')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
    elif resposta == 3:
        # Sai do sistema
        cabeçalho('Saindo do sistema... até logo!')
        sleep(1)
        break
    else:
        # Caso o usuário digite errado
        print('\033[31m[ ERRO ], Digite uma opção válida!\033[m')
    sleep(1)


