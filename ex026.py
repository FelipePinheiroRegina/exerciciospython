frase = str(input('Digite uma frase: ')).upper().strip()
print('\033[1;41m A letra "A" aparece {} vezes \033[m'.format(frase.count('A'))) #Conta Quantas letras A
print('\033[1;42m A primeira letra "A" aparece na posição {}° \033[m'.format(frase.find('A')+1)) #Indica onde a primeira letra A começa.
print('\033[1;43m A última letra "A" aparece na posição {}° \033[m'.format(frase.rfind('A')+1 - frase.count(' '))) #Indica onde a ultima letra A começa.