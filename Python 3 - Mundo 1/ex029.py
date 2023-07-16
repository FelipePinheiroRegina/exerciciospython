print('\033[1;32m==========\033[m\033[1;30m(RADAR)\033[m\033[1;32m=============\033[m')
print('      \033[1;31mLimite do Radar         ')
print('         \033[1;31m(80 km/H)            ')
print('\033[1;32m==============================\033[m')
vel = int(input('\033[36mKm / H: \033[m'))
if vel > 80:
    print('\033[1;31mSua Velocidade: {}Km / H'.format(vel))
    print('MULTADO POR EXCESSO DE VELOCIDADE!')
    multa = (vel - 80) * 7.00
    print('Valor da Multa: R$ {:.2f}'.format(multa))
else:
    print('\033[1;32mSua Velocidade: {}Km / H'.format(vel))
    print('Velocidade dentro dos limites!\nUse cinto de segurança!\nBoa Viagem!')