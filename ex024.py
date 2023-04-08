'''cid = input('Digite o Nome de uma cidade: ')
cidade = cid.split()
print('Cidade digitada {} \nComeça com o nome "SANTO"? {}'.format(cid, 'santo' in cidade[0].lower()))
'''
'''cidade = str(input('Nome da Cidade: ')).strip()
cid = cidade.split()
c = 'SANTO' in cid[0].upper()
print('Começa com santo?: {}'.format(c))
'''
cid = str(input('Em que cidade nasceu?: ')).strip()
if cid[0:5].upper() == 'SANTO':
    print('\033[1;32m VERDADEIRO!')
else:
    print('\033[1;31m FALSO!')

