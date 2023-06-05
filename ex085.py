'''principal = impar = par = list()
for c in range(7):
    principal.append(int(input(f'Digite o {c + 1}° valor: ')))
impar.sort()
for v in impar:
    if v % 2 == 1:
        print(f'( {v} ) ', end='')
print()
par.sort()
for v in par:
    if v % 2 == 0:
        print(f'( {v} ) ', end='')'''
principal = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c + 1}° número: '))
    if n % 2 == 0:
        principal[0].append(n)
    else:
        principal[1].append(n)
principal[0].sort()
principal[1].sort()
print(f'Os valores pares da lista foram: {principal[0]}')
print(f'Os valores impares da lista foram: {principal[1]}')
