import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('{}O aluno escolhido foi {}.'.format('\033[1;35m', escolhido))
