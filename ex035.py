'''Digite tres retas, e eu quero saber de da pra formar um triangulo com as 3 retas digitadas'''

print('\033[36m---'*10)
print(' '*3,'Formador de Triangulos')
print('---'*10)
print('Digite o tamanho de cada reta')
a = int(input('Reta a: '))
b = int(input('Reta b: '))
c = int(input('Reta c: '))

if a + b > c and a + c > b and c + b > a:
    print('Com essas retas você pode formar um triangulo')
else:
    print('Com essas retas você não consegue formar um triangulo')