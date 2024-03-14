# Exercício Python #021 - Tocando um MP3 - Aulas 00 até 08 - Mundo 1
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
from emoji import emojize
arquivo = 'C:/Users/mdbsi/OneDrive/Documentos/GitHub/meus-estudos/cursoemvideo_python/dezembro/Exercicios/audio.mp3'

pygame.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
pygame.event.wait()

print(emojize(':notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais:', language='pt'))
input("Pressione Enter para sair...")  # Mantém o programa em execução até que Enter seja pressionado
