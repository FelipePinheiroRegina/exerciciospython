'''
Crie um programa que tenha uma tupla com varias palavras
(não usar acentos), depois disso, você deve mostrar, para
cada palavra, quais são suas vogais.
'''
Palavras = ('Python', 'polegar')

for c in range(0, len(Palavras)):
    print(Palavras[c])
    if Palavras[c] in 'aeiouAEIOU':
        print(Palavras.count('o')[c])