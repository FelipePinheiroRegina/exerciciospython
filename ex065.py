'''
Crie um programa que leia vários números inteiros pelo teclado.
no final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lido. o programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
'''
#Meu código
'''soma = 0
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
print(média, maior, menor)'''

#Código Professor
resp = 'S'
média = soma = cont = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma = soma + núm
    cont = cont + 1
    if cont == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        elif núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / cont
print('A média de {} dividido por {} é {}.'.format(soma, cont, média))
print('O Maior número digitado foi {}, e o Menor foi {}.'.format(maior, menor))


