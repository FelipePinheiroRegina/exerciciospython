ficha = list()
while True:
    nome = str(input('Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0].capitalize():<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opção == 999:
        break
    if opção <= len(ficha):
        print(f'Aluno {ficha[opção][0].capitalize()}, Notas: {ficha[opção][1]}')