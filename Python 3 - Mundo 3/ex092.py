from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contrato'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Sálario R$: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contrato'] + 35) - datetime.now().year)

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

