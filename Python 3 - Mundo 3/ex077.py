'''
Crie um programa que tenha uma tupla com varias palavras
(não usar acentos), depois disso, você deve mostrar, para
cada palavra, quais são suas vogais.
'''
palavras = ('Python', 'JavaScript', 'Java', 'Felipe', 'Programador', 'FullStack', 'OlaMundo', 'HellowWorld')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')