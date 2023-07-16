time = list()
gols = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))

    for p in range(partidas):
        gols.append(int(input(f'    Quantos gols na {p+1}: ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()

    resposta = str(input('Deseja continuar? [S/N]: ')).upper()
    if resposta in 'N':
        break

print('-=' * 30)
print(f'{"Cod":>4} {"Nome":<15} {"Gols":<15} {"Total":<15}')
print('--' * 26)
for i, v in enumerate(time):
    print(f'{i:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)
while True:
    opçao = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if opçao == 999:
        break
    elif opçao <= len(time):
        print(f'    ---LEVANTAMENTO DO JOGADOR {time[opçao]["nome"]}')
        for i, p in enumerate(time[opçao]['gols']):
            print(f'    No jogo {i+1} fez {p} gols.')
    print('-' * 26)



