'''matriz = [[],
          [],
          []]
for m in range(len(matriz)):
    if m == 0:
        for c in range(3):
            matriz[0].append(int(input(f'Digite o valor da posição [{m}, {c}]: ')))
    elif m == 1:
        for c in range(3):
            matriz[1].append(int(input(f'Digite o valor da posição [{m}, {c}]: ')))
    else:
        for c in range(3):
            matriz[2].append(int(input(f'Digite o valor da posição [{m}, {c}]: ')))
for p in matriz[0]:
    print(f'[ {p:^5} ]', end='')
print()
for p in matriz[1]:
    print(f'[ {p:^5} ]', end='')
print()
for p in matriz[2]:
    print(f'[ {p:^5} ]', end='')'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um número para posição [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
