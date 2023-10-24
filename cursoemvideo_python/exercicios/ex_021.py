"""Desafio 021 - Tocando um mp3 (Aula 01 a 09): Faça um programa em python que abra o áudio de um arquivo mp3.
"""

# 1. **Instale a biblioteca pygame**: Certifique-se de que a biblioteca pygame está instalada no seu ambiente Python. Você pode instalá-la usando o pip:

# pip install pygame

# 2. **Importe a biblioteca pygame**: No início do seu código, importe a biblioteca pygame:
import pygame

# 3. **Inicialize o pygame**: Antes de usar qualquer recurso do pygame, é necessário inicializá-lo:

pygame.init()

# 4. **Carregue o arquivo MP3**: Use o método `pygame.mixer.music.load()` para carregar o arquivo MP3 que você deseja reproduzir:

pygame.mixer.music.load("ex01.mp3")

# 5. **Inicie a reprodução**: Use o método `pygame.mixer.music.play()` para iniciar a reprodução do arquivo MP3:

pygame.mixer.music.play()
pygame.event.wait()
# 6. **Controle a reprodução (opcional)**: Você pode controlar a reprodução, como pausar, parar e ajustar o volume, usando as funções apropriadas do módulo `pygame.mixer.music`.

# 7. **Aguarde o término da reprodução** (opcional): Se você deseja esperar até que a música termine de tocar, pode usar `pygame.mixer.music.get_busy()` em um loop para verificar se a música está tocando.

# 8. **Finalize o pygame**: Quando terminar de usar o pygame, certifique-se de finalizá-lo:

# pygame.quit()
