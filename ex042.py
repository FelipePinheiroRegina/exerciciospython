'''
Refaça o exercicio 35 dos triangulos
acrescentando o recurso de mostrar
que tipo de triangulo sera formado:

- Equilatero todos lados iguais
- isóceles dois lados iguais
- escaleno todos lados diferentes
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
