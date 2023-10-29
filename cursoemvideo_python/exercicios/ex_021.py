"""Desafio 021 - Tocando um mp3 (Aula 01 a 08): Faça um programa em python que abra o áudio de um arquivo mp3.
"""

# 1. **Instale a biblioteca pygame**: Certifique-se de que a biblioteca pygame está instalada no seu ambiente Python. Você pode instalá-la usando o pip:

import pygame

# Inicializa o pygame
pygame.init()

# Caminho para o arquivo MP3 que você deseja reproduzir
mp3 = 'ex01.mp3'

# Carrega o arquivo MP3
pygame.mixer.music.load(mp3)

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Aguarda até que a música termine de tocar
while pygame.mixer.music.get_busy():
    pass

# Finaliza o pygame
pygame.quit()
