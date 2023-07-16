'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarda-os em uma tupla. no final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares
'''
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
v3 = int(input('Digite um valor: '))
v4 = int(input('Digite um valor: '))
Valores = (v1, v2, v3, v4)
print(f'Quantas vezes apareceu o Valor [ 9 ]: {Valores.count(9)}.')
if 3 in Valores:
    print(f'O primeiro Valor [ 3 ] apareceu na {Valores.index(3)+1}° Posição.')
else:
    print('O Valor 3 não foi digitado.')
print('Os Valores Pares foram', end=' ')
for c in range(0, 4):
    if Valores[c] % 2 == 0:
        print(Valores[c], end=' ')

#núm = (int(input('Digite um número: ')), int(input('Digite um número: ')),
#        int(input('Digite um número: ')), int(input('Digite um número: '))) # Da para armazenar varios valores digitado pelo usuario assim.
#print(núm)
