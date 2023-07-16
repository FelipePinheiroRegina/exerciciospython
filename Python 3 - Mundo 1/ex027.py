nome = str(input('Nome completo: ')).strip()
nc = nome.split()
print('Seu primeiro nome é \033[4;36m {} \033[m'.format(nc[0]))
print('seu último nome é \033[4;35m {} \033[m'.format(nc[len(nc)-1])) # pega a v.split e mostra o ultimo comprimento dela - 1

