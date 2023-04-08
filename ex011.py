print('==========PAREDE======================')
Largura = float(input('Quanto de Largura: '))
Altura = float(input('Quanto de Altura: '))
Area = Largura * Altura
print('A parede tem {}{}{} x {}{}{}, e sua Área é de {}{}m²{}.'.format('\033[1;35m', Largura, '\033[m', '\033[1;32m', Altura, '\033[m', '\033[1;33m', Area, '\033[m'))
tinta = Area / 2
print('Voçê precisará de {}{}{} L, de tinta para pintar esta Área.'.format('\033[31m', tinta, '\033[m'))