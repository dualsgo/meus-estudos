"""Desafio 087 -  (Aula 01 a 18): Aprimore o desafio anterior, mostrando no final.
- A soma de todos os valores pares digitados
- A soma dos valores da terceira coluna
- O maior valor da segunda linha
"""
matriz = []

# Loop para preencher a matriz
for i in range(3):
    linha = []  # Inicializa uma nova linha vazia
    for j in range(3):
        numero = int(input(f'Digite um valor para [{i+1}][{j+1}]: '))
        linha.append(numero)
    matriz.append(linha)

# Exibe a matriz entre colchetes
for linha in matriz:
    print(f'[{linha[0]}] [{linha[1]}] [{linha[2]}]')

# A soma de todos os valores pares digitados
soma_pares = 0
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            soma_pares += numero
print(f'A soma de todos os valores pares digitados é: {soma_pares}')

# A soma dos valores da terceira coluna
soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma de todos os valores da terceira coluna é: {soma_terceira_coluna}')

# O maior valor da segunda linha
maior_segunda_linha = max(matriz[1])
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')

