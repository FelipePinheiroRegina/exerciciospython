m = float(input('\033[4;31;47mConversor de Metros para cm, mm: \033[m'))
cm = m * 100
mm = m * 1000
print('\033[31m{:.0f}m\033[m, tem \033[35m{:.0f}cm\033[m, \033[32m{:.0f}mm.\033[m'.format(m, cm, mm))