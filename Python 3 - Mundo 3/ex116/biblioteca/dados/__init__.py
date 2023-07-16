from ex116.biblioteca.visual import *

def verificaArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print('\033[31m[ ERRO AO CRIAR O ARQUIVO ]\033[m')
    else:
       print('\033[32m==> ARQUIVO CRIADO\033[m')
    finally:
        a.close()


def verPessoas(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('[ ERRO AO MOSTRAR PESSOAS CADASTRADAS.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrarPessoa(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('[ ERRO AO CADASTRAR PESSOA')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('[ ERRO AO DIGITAR O NOME DA PESSOA ]')
        else:
            print(f'{nome} cadastrado(a) com sucesso.')
    finally:
        a.close()

