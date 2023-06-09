lista_de_pessoas = []
pessoas = dict()
while True:
    pessoas['nome'] = str(input('Nome: ')).capitalize()
    sexo = str(input('Sexo [ M / F ]: ')).upper()
    while sexo not in 'MF':
        print('ERRO, Por favor, digite apenas M ou F!')
        sexo = str(input('Sexo [ M / F ]: ')).upper()
    pessoas['sexo'] = sexo
    idade = int(input('Idade: '))
    pessoas['idade'] = idade
    lista_de_pessoas.append(pessoas.copy())
    termina_programa = str(input('Deseja cadastrar mais pessoas? [ S / N ]: ')).upper()
    while termina_programa not in 'SN':
        print('ERRO, Por favor, digite apenas S ou N!')
        termina_programa = str(input('Deseja cadastrar mais pessoas? [ S / N ]: ')).upper()
    if termina_programa in 'N':
        break
print('-=' * 30)
print(f'A) Ao todo Temos {len(lista_de_pessoas)} pessoas cadastradas.')

# Pegando a média de idade
totalidade = 0
for pessoa in lista_de_pessoas:
    totalidade += pessoa['idade']
média = totalidade / len(lista_de_pessoas)
print(f'B) A média de idade é de {média:.2f} anos.')
# -----------------------------------------------

# Pegando mulheres cadastradas
print('C) As mulheres cadastradas foram, ', end='')
for i, pessoa in enumerate(lista_de_pessoas):
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print()
# -----------------------------------------------

# Pegando as pessoas que tem a idade a cima da média de idade
print('D) Lista das pessoas que estão acima da média:')
for pessoa in lista_de_pessoas:
    if pessoa['idade'] > média:
        print(f'    Nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]};')
print('<< ENCERRADO >>')

