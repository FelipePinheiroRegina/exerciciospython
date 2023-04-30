'''
Crie uma tupla preenchida com os 20 primeiros colocados
da tablea do campeonato brasileiro de futebol
na ordem de colocaçõa, e depois mostra:
A)Apenas os 5 primeiros colocados
B)Os ultimos 4 colocados da tabela
C)Uma lista com os time em ordem alfabetica
D)Em que posição da tabela está o time da chapecoense
'''
Times = ('Fortaleza', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Botafogo', 'São Paulo', 'Vasco', 'Internacional', 'Atlético-MG', 'Santos', 'Bragantino', 'Flamengo', 'Goiás', 'Grêmio', 'Athletico-PR', 'Corinthians', 'Cuiabá', 'Coritiba', 'Bahia', 'América-MG')
print(f'TABELA BRASILEIRÃO 2023')
print(Times)
print('====='*50)
print(f'O [ TOP 5 ] dos primeiros colocados na Tabela do Brasileirão 2023 são:\033[34m{Times[0:5]}\033[m')
print(f'O [ TOP 4 ] dos últimos colocados na Tabela do Brasileirão 2023 são:\033[31m{Times[-4:]}\033[m')
print(f'Os Times do Brasileirão 2023 em ordem alfabética.')
print(sorted(Times))
print('O Time do São Paulo está na {}° Posição!'.format(Times.index('São Paulo')+1))
