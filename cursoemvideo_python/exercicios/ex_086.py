"""Desafio 086 -  (Aula 01 a 18): Crie um programa que crie uma matriz de dimensão de 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela com a formatação correta.
[1] [2] [3]
[4] [5] [6]
[7] [8] [9]
"""

# Inicializa uma matriz vazia
matriz = []

# Preenche a matriz com valores lidos pelo teclado
for i in range(3):
    linha = []  # Inicializa uma nova linha vazia
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i+1}][{j+1}]: '))
        linha.append(valor)
    matriz.append(linha)

# Exibe a matriz na tela com a formatação correta
for linha in matriz:
    print('[', end='')  # Início da linha
    for valor in linha:
        print(f'[{valor}]', end=' ')  # Exibe cada valor entre colchetes e separados por espaço
    print(']')  # Fim da linha


