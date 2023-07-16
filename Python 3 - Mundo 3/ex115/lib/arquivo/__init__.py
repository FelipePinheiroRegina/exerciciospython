from interface import *
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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()



def cadastrarPessoa(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao cadastrar uma nova pessoa')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever o nome.')
        else:
            print(f'{nome} cadastrado(a) com sucesso.')
            a.close()

