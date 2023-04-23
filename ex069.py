'''
Crie um programa que leia a idade e o sexo de varias pessoas
a cada pessoa cadastrada o programa deverá perguntar se o usuario quer
ou não continuar, no final mostre,
# quantas pessoas tem mais de 18
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos
'''
qtsmais18 = mcadastrado = qtsfmenos20 = 0
print('~'*20)
print('Cadastro de Pessoas')
print('~'*20)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo = [ M / F ]: ')).upper().strip()[0]
    while not sexo in 'M F':
        print('Sexo invalido! digite novamente.')
        sexo = str(input('Sexo = [ M / F ]: ')).upper().strip()[0]
    if idade > 18:
        qtsmais18 = qtsmais18 + 1
    if sexo == 'M':
        mcadastrado = mcadastrado + 1
    if idade < 20 and sexo == 'F':
        qtsfmenos20 = qtsfmenos20 + 1
    print('Pessoa cadastrada!')
    opçao = str(input('Quer continuar? [ S / N ]: ')).upper().strip()[0]
    while not opçao in 'S N':
        print('Opção invalida, por favor digite [ S / N ]')
        opçao = str(input('Quer continuar? [ S / N ]: ')).upper().strip()[0]
    if opçao == 'N':
        break
print(f'Existem {qtsmais18} pessoas maiores que 18 anos.')
print(f'Existem {mcadastrado} homens cadastrados.')
print(f'Existem {qtsfmenos20} mulheres menores de 20 anos.')


