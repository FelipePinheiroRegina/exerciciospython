'''Crie um programa que leia uma frase
qualquer e diga se ela é um palindromo
desconsiderando os espaços'''
# (EX de palindromo)
'''
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''
frase = str(input('Digite uma frase: ')).upper()
frasefatiada = frase.split()
frasesemespaço = ''.join(frasefatiada)
inverso = frasesemespaço[::-1]
'''for c in range(len(frasesemespaço) -1, - 1, - 1):
    inverso += frasesemespaço[c]'''
print('Frase digitada foi {}, e o inverso dela é {}.'.format(frasesemespaço, inverso))
if frasesemespaço == inverso:
    print('Temos um Palindromo!.')
else:
    print('A frase digitada não é um Palindromo!.')