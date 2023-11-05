"""Desafio 047 - Contagem de pares (Aula 01 a 13): Crie um programa que mostre na tela todos os números pares que estiverem entre 1 e 50."""
# Definimos a variável pares como uma lista vazia que irá receber os valores que atenderem a condição
pares = []
impares = []

# Definir o intervalo entre 1 e 50
for i in range(1, 51):
    # Avaliar se o número é par. Verificamos se o resto da divisão por 2 será 0
    if i % 2 == 0:
        # Adicionamos os valores que atenderem a condição a uma lista
        pares.append(i)
    else:
        impares.append(i)

# Imprimir os valores pares sem colchetes
print('\033[32mOs valores pares são:\033[m', end=' ')
for numero in pares:
    print(numero, end=', ')
print('e fim.')  # Para imprimir uma quebra de linha

# Se você quiser imprimir os valores ímpares da mesma maneira, pode fazer o mesmo para a lista impares
print('\033[31mOs valores ímpares são:\033[m', end=' ')
for numero in impares:
    print(numero, end=', ')
print('e fim.')  # Para imprimir uma quebra de linha