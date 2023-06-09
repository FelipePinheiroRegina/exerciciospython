jogador = dict()
golporpartida = []
soma = 0
jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(partidas):
    golporpartida.append(int(input(f'    Quantos gols na {c + 1}° Partida: ')))
    soma += golporpartida[c]
jogador['gols'] = golporpartida
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas!')
for i, p in enumerate(golporpartida):
    print(f'   ==> Na {i + 1}° Partida ele fez {p} Gols.')
print(f'Foi um total de {jogador["total"]} Gols.')
