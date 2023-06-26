def alunos(* n, sit=False):
    '''
    ==> SALA DE AULA / ESTÁCIO 2023 / CIÊNCIA DA COMPUTAÇÃO.
    :param n: Notas dos alunos, pode ser uma, duas ou dez.
    :param sit: Se Verdadeiro, mostre a situação: RUIM, RAZOÁVEL, BOA; de acordo com a média da classe.
    :return: Um Dicionario com o total de notas, a maior e menor nota, a média, a situação se verdadeira.
    '''
    m = sum(n) / len(n)
    turma = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': m}
    if sit:
        if m < 5:
            turma['situação'] = 'RUIM'
        elif 5 <= m < 7:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOA'
    return turma


# Programa principal
resultado = alunos(3, 5, 7.6, 8.4, 9.2, 10, 3.4, 1.2, sit=True)
print(resultado)
help(alunos)
