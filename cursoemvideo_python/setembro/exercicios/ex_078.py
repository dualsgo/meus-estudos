"""
Desafio 078 - Maior e menores valores da lista (Aula 01 a 17): Faça um programa que leia cinco valores numéricos e guarde-os em uma lista. No final, mostre qual foi o menor e o maior valor digitado e as suas respectivas posições na lista. Mostrar se houver mais de uma posição
"""
# Inicializar as listas
lista = []              # Lista para armazenar os valores digitados
posicao_menor = []      # Lista para armazenar as posições do menor valor
posicao_maior = []      # Lista para armazenar as posições do maior valor

# Ler cinco valores numéricos e guardá-los em uma lista.
for posicao in range(5):  # Loop para pedir cinco valores
    elemento = int(input(f'Digite o valor numérico da posição {posicao}: '))  # Solicita um valor e converte para inteiro
    lista.append(elemento)  # Adiciona o valor à lista

print(f'Você digitou os valores: {lista}')  # Exibe a lista completa

# Encontrar as posições do menor e do maior valor na lista
for posicao, valor in enumerate(lista):  # Loop para percorrer a lista com índices e valores
    if valor == min(lista):  # Se o valor atual é igual ao menor valor na lista
        posicao_menor.append(posicao)  # Adiciona a posição à lista de posições do menor valor
    if valor == max(lista):  # Se o valor atual é igual ao maior valor na lista
        posicao_maior.append(posicao)  # Adiciona a posição à lista de posições do maior valor

# Mostrar o maior e o menor valor digitado e o seu índice
print(f'O menor valor é {min(lista)}. Aparece em: {posicao_menor}')  # Exibe o menor valor e suas posições
print(f'O maior valor é {max(lista)}. Aparece em: {posicao_maior}')  # Exibe o maior valor e suas posições

################# MÉTODO DO GUANABARA

listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O menor valor digitado foi o {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')