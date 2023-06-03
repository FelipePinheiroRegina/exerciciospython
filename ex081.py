'''
Crie um program que vai ler vários números
e colocar em uma lista.
depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma
decrescente
C) Se o valor 5 foi digitado e está ou não
na lista
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Você digitou {len(valores)} valores!')
valores.sort(reverse=True)
for v in valores:
    print(f'{v}.. ', end='')
if 5 in valores:
    print('\nO cinco faz parte dos valores!')
else:
    print('\nNão encontrei o cinco entre os valores!')