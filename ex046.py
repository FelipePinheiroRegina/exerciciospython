'''Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artificio, indo de 10 até 0,
com uma pausa de 1 segundo entre eles'''
from time import sleep
import emoji
print('\033[1;35m{:=^70}\033[m'.format(' CONTAGEM PARA O ESTOURO DE FOGOS '))
for c in range(10, 0 - 1, - 1):
    print(c, '...')
    sleep(1)
print('\033[1;31mESTOUROS DE FOGOS!!!!!\033[m')
sleep(1)
print(emoji.emojize(':Sparkles::Sparkles::Sparkles::Sparkler::Sparkler::Sparkler::Fireworks::Fireworks::Fireworks::Fire::Fire::Fire:'.lower()))