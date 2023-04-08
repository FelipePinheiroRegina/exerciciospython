print('\033[34;40m--- Jogo: Ímpar x Par ---\033[m')
num = int(input('\033[34mNúmero: '))
if num % 2 == 0:
    print('\033[1;32mNúmero Par')
else:
    print('\033[1;31mNúmero Ímpar')
