"""Desafio 080 -  (Aula 01 a 17): Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela. Mostrar se foi adicionado no final da lista se for o maior que os já digitados ou a posição se for menor
"""
lista = []
for posicao in range(5):
    elemento = int(input('Digite um valor: '))
    if elemento > lista[posicao]:
        lista.append(elemento)
        print('Elemento adicionado no fim.')
    elif elemento < lista[posicao]:
        lista.insert(0, elemento)
        print('Elemento adicionado no início.')
print(lista)