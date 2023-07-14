from visual import *
from dados import *


arquivo = 'cadastro.txt'
if not verificaArquivo(arquivo):
    criarArquivo(arquivo)

while True:
    cabeçalho('SISTEMA DO FELIPE')
    opção = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Finalizar sistema'])
    if opção == 1:  # VER AS PESSOAS CADASTRADAS NO SISTEMA
        verPessoas(arquivo)
    elif opção == 2:  # CADASTRAR UMA NOVA PESSOA NO SISTEMA
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrarPessoa(arquivo, nome, idade)
    elif opção == 3:  # SAIR DO SISTEMA
        print(f'VOCÊ ESCOLHEU A OPÇÃO {opção}')
        break
    else:  # ERRO, O USUÁRIO DIGITOU ALGO ERRADO.
        print('[ ERRO ] digite uma opção válida.')


