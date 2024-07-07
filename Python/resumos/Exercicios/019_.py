import random

lista = [1, 2, 3, 4, 5, 1, 0, 2, 4, 3]

# Sortear 3 vezes sem repetir os elementos
for _ in range(3):
    sorteio = random.sample(lista, 3)  # Sortear 3 elementos únicos da lista
    print('Os alunos sorteados são:', sorteio)