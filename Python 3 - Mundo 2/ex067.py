'''
Faça um programa que mostre a tabuada de varios números. um de cada vez
para cada valor digitado pelo usuário, o programa
será interrompido quando o número solicitado for negativo.
'''
print('=-='*10)
print('FORMADOR DE TABUADA')
print('=-='*10)
while True:
    tabuada = int(input('Qual tabuada você deseja? '))
    if tabuada < 0:
        break
    print('=-=' * 10)
    for c in range(1, 10 + 1):
        print(f'{tabuada} x {c:>2} = {tabuada * c}')
    print('=-=' * 10)
print('TABUADA FINALIZADA!')
