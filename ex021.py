import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('ex021')
print('\033[1;32m Carregando pedrada! \033[m')
sleep(3)
pygame.mixer.music.play()
input()
pygame.event.wait()