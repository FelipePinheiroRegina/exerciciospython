from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # Tenta abrir um arquivo,  o "rt" significa "read, text"
        a.close()  #  Fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # Tenta abrir um arquivo,  o "wt" significa "write, text",
        a.close()               # e o + = se não tiver nenhum arquivo com esse nome, ele cria
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerPessoas(pessoas):
    try:
        a = open(pessoas, 'rt')
    except:
        print('ERRO, ao mostrar as pessoas cadastradas.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())

