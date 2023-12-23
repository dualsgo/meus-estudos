"""Desafio 080 - Lista ordenada sem repetições (Aula 01 a 17): Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela. Mostrar se foi adicionado no final da lista se for o maior que os já digitados ou a posição se for menor
"""
from random import randint
# Inicializar a lista
lista = []

# Loop para solicitar cinco valores numéricos
for posicao in range(5):
    # Solicitar um valor numérico ao usuário
    elemento = randint(0, 9)

    # Verificar se a lista está vazia
    if not lista:
        # Se estiver vazia, adicionar o elemento no início
        lista.append(elemento)
        print(f'Elemento adicionado no início, na posição {lista.index(elemento)}.')
    else:
        # Se não estiver vazia
        # Verificar onde o elemento deve ser adicionado
        if elemento > max(lista):
            # Se for maior que todos os elementos, adicionar no fim
            lista.append(elemento)
            print(f'Elemento adicionado no fim, na posição {lista.index(elemento)}.')
        elif elemento < min(lista):
            # Se for menor que todos os elementos, adicionar no início
            lista.insert(0, elemento)
            print(f'Elemento adicionado no início, na posição {lista.index(elemento)}.')

# Exibir a lista ordenada
print(lista)


########## Guanabara

lista = []
for c in range(0, 5):
    n = randint(0, 9)
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
