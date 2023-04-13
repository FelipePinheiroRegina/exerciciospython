'''Desenvolva um programa que leia o
primeiro termo e a razão de uma PA. no final, mostre
termos dessa progressão'''
print('='*10)
print('{:^10}'.format('P.A'))
print('='*10)
termo = int(input('Qual é o Primeiro Termo, (a1), da P.A: '))
razao = int(input('Qual é a razão da PA: '))
if razao > 0:
    for c in range(1, 5 + 1):
        print(termo, end=', ')
        termo += razao
    print('\n(P.A CRESCENTE)')
elif razao == 0:
    for c in range(1, 5 + 1):
        termo = termo
        print(termo, end=', ')
    print('\n(P.A CONSTANTE)')
else:
    for c in range(1, 5 + 1):
        print(termo, end=', ')
        termo += razao

    print('\n(P.A DECRESCENTE)')




