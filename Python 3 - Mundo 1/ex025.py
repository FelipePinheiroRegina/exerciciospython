nome = input('Digite seu Nome Completo: ').strip()
print('Tem \033[1;34m "Silva" \033[m no nome? {}.'.format('SILVA' in nome.upper()))