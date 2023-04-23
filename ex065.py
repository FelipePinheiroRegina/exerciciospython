'''
Crie um programa que leia vários números inteiros pelo teclado.
no final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lido. o programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
'''
soma = 0
cont = 0
média = 0
maior = 0
menor = 1000000000000
c = 1
print('Para finalizar digite 0')
while c != 0:
    num = int(input('Número: '))
    if num != 0:
        soma += num
        cont += 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if num == 0:
        finalizar = str(input('Realmente deseja finalizar?: [S/N] ')).upper()
        if finalizar == 'S':
            c = num
média = soma / cont
print(média, maior, menor)
