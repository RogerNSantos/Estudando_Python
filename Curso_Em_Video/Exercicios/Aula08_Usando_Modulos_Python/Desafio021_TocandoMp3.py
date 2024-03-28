""" Faça um programa  em Python que abra e reproduz o áudio de um arquivo MP3. """

import pygame

pygame.init()
pygame.mixer.music.load("nome do arquivo, arquivo deve está dentro da mesma pasta!")
pygame.mixer.music.play()
pygame.event.wait()

