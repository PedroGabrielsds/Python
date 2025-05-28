#Ex046 - Aula 13

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de um segundo entre eles.

from time import sleep
from traceback import clear_frames

for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
import pygame

pygame.init()
pygame.mixer.music.load('ex046.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()