import math
num = float(input('Digite um número?: '))
n = math.trunc(num)
print('\033[30;46m O número digitado em sua porção maior é {}, quando usamos a função trunc, fica {}.'.format(num, n))