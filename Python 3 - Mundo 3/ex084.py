pessoas = list()
dados = list()
maior = menor = 0
print('REGISTRADOR DE PESSOAS')
print('=-' * 30)
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: [ex: 85.2] ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Entrar com mais Pessoas? [ S / N] '))
    if resposta in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo, foram {len(pessoas)} pessoas cadastradas!')
print(f'O maior peso foi {maior}Kg. das pessoas => ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'( {p[0].capitalize()} ) ', end='')
print()
print(f'O menor peso foi {menor}Kg. das pessoas => ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'( {p[0].capitalize()} ) ', end='')



