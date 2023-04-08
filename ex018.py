import math
num = float(input('\033[1;34m Digite um Ângulo: \033[m'))
seno = math.sin(math.radians(num))
coseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print('\033[1;31m O Ângulo digitado é {}. \033[m'.format(num))
print('\033[1;36m Seu Seno é {:.2f}. \033[m'.format(seno))
print('\033[1;32m Seu Coseno é {:.2f}. \033[m'.format(coseno))
print('\033[1;35m Sua Tangente é {:.2f}. \033[m'.format(tangente))

