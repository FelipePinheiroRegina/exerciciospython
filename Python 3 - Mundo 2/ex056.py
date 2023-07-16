'''desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas. no final
do programa, e mostre:
a media de idade do grupo
qual é o nome do homem mais velho
quantas mulheres tem menos de 20 anos'''
média = 0
soma = 0
cont = 0
maior = 0
nomemaisvelho = ''
contM = 0
for c in range(1,5):
    nome = input('{}° Nome: '.format(c))
    idade = int(input('Idade: '))
    sexo = input('Sexo: (M) ou (F) ').upper()
    soma += idade
    cont += 1
    if idade > maior and sexo in 'M':
        maior = idade
        nomemaisvelho = nome
    if sexo in 'F' and idade < 20:
        contM += 1
média = soma / cont
print('''A média do grupo é {}.
O homem mais velho chama-se {}.
Existem {} mulheres abaixo de 20 anos no grupo.
'''.format(média, nomemaisvelho, contM))
