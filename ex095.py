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
print(f'{"Cod":<3} {"Nome":<10} {"Gols":<10} {"Total":>8}')
print('--' * 26)
for i, j in enumerate(time):
    print(f"{i:<3} {j['nome']:<10} {j['gols'][0:]:<10} {j['total']:>8}")



