# Faça um programa em Python que abra e reprduza o áudio de um arquivo em MP3
print('******** DESAFIO - AULA 08 - REPRODUÇÃO DE MP3 *********')
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
