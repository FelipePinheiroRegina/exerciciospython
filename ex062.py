'''
Melhore o desafio 061m perguntando
ppara o usuário se ele quer mostrar mais
alguns termos. o programa encerra quando ele
disser que quer mostrar 0 Termos.
'''
p1 = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))
cont = 10
while cont != 0:
    print('{}'.format(p1), end=' ')
    p1 += razao
    cont -= 1
    if cont == 0:
        cont = int(input('Quer ver mais quantos termos? '))
