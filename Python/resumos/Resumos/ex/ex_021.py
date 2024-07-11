# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
from emoji import emojize
arquivo = 'C:/Users/mdbsi/OneDrive/Área de Trabalho/meus-estudos/Python/resumos/Resumos/ex/audio.mp3'

pygame.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
pygame.event.wait()

print(emojize(':notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais:', language='pt'))
input("Pressione Enter para sair...")  # Mantém o programa em execução até que Enter seja pressionado