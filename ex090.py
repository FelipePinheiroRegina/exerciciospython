aluno = dict()
aluno['nome'] = str(input('Digite o seu nome: '))
aluno['média'] = float(input(f'Digite a média do {aluno["nome"].capitalize()}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} do Aluno é igual a {v}')
