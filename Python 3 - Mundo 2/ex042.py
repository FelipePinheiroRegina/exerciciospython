#Critérios
'''
Refaça o exercicio 35 dos triangulos
acrescentando o recurso de mostrar
que tipo de triangulo sera formado:

- Equilatero todos lados iguais
- isóceles dois lados iguais
- escaleno todos lados diferentes
'''
# Meu código
'''
print('\033[1;31m=-=-=-=-=-=-=-=-='*5)
print('                                Forme um Triangulo')
print('=-=-=-=-=-=-=-=-='*5, '\033[m')
a = float(input('Linha a: '))
b = float(input('Linha b: '))
c = float(input('Linha c: '))

if a + b > c and a + c > b and b + c > a:
    print('Com essas linhas da para formar um triângulo')
    if a == b and a == c and b == c:
        print('Três linhas iguais formam um triângulo\033[1;35m Equilatero \033[m')
    elif a == b or a == c or b == c:
        print('Duas Linhas iguais formam um triângulo\033[1;32m Isóceles\033[m')
    elif a != b and a != c and b != c:
        print('Tres linhas diferentes formam um triângulo\033[1;34m Escaleno \033[m')
else:
    print('Com essas linhas não da pra formar um triângulo')
'''

# Código do professor

print('Forme um Triangulo!')
r1 = float(input('1° Segmento: '))
r2 = float(input('2° Segmento: '))
r3 = float(input('3° Segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[1;32mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;31mESCALENO!\033[m')
    else:
        print('\033[1;34mISÓCELES!\033[m')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo!')
