'''
crie um programa que leia duas notas de um
aluno que calcule sua média, mostrando
uma mensagem no final, de acordo com a média
atingida

 CRITERIOS
 - MEDIA ABAIXO DE 5.0 == REPROVADO
 - MEDIA ENTRE 5.0 E 6.9 == RECUPERAÇÃO
 - MEDIA MAIOR QUE 7.0 == APROVADO
'''
from time import sleep
nota1 = float(input('1° Nota: '))
nota2 = float(input('2° Nota: '))
media = (nota1 + nota2) / 2

print('\033[1;35m VERIFICANDO...(APROVAÇÃO - RECUPERAÇÃO - REPROVAÇÃO) \033[m')
sleep(3)

if media <= 5.0:
    print('Média: \033[1;31m{}\033[m'.format(media))
    print('\033[1;31m [REPROVADO] estude mais! \033[m')
elif media > 5.0 and media < 6.9:
    print('Média: \033[1;34m{}\033[m'.format(media))
    print('\033[1;34m [RECUPERAÇÃO] não pare de estudar! \033[m')
elif media > 7.0:
    print('Média: \033[1;32m{}\033[m'.format(media))
    print('\033[1;32m [APROVADO] Parabéns, mas isso é só o começo, estude sempre! \033[m')