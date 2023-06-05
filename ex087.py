matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = terceiracoluna = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o número da posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        #if matriz[l][c] == matriz[0][2] or matriz[l][c] == matriz[1][2] or matriz[l][c] == matriz[2][2]:
         #    terceiracoluna += matriz[l][c]
        #if l == 1:
         #   if matriz[l][c] > maior:
         #       maior = matriz[l][c]
print('-' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-' * 30)
print(f'A soma dos pares é {soma}')
for l in range(3):
    terceiracoluna += matriz[l][2]
print(f'A soma da terceira coluna é {terceiracoluna}')
for c in range(3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')



