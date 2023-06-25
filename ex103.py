'''

def ficha(N_Jogador, N_Gols=0):
    if N_Jogador == "":
        N_Jogador = "<desconhecido>"
    if N_Gols != type(int):
        N_Gols = 0
    return f"O Jogador {N_Jogador} fez {N_Gols} gol(s) no campeonato."


# Programa Principal
print('*' * 20)
nome = str(input('Nome do Jogador: '))
gols = input('Número de Gols: ')
print(ficha(nome, gols))
'''


def ficha(nome='<desconhecido>', gols=0):
    print(f'O Jogador {nome} fez {gols} gol(s) na partida.')


Nome = str(input('Nome do Jogador: '))
Gols = str(input('Número de Gols: '))
if Gols.isnumeric():
    Gols = int(Gols)
else:
    Gols = 0
if Nome.strip() == '':
    ficha(gols=Gols)
else:
    ficha(Nome, Gols)
