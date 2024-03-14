# Exercício Python #078 - Maior e Menor valores na Lista - Aula 00 até 17 - Mundo 3
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


# Inicializa uma lista vazia
lista = []

# Obtém a entrada do usuário para cada índice
for contador in range(5):
    lista.append(int(input(f'Digite o valor do índice {contador}: ')))

# Encontra as posições dos elementos mínimo e máximo
maior = [indice for indice, elemento in enumerate(lista) if elemento == max(lista)]
# indice: Adiciona o índice do elemento atual à lista maior se a condição for verdadeira.
# enumerate(lista): Esta função retorna tuplas contendo pares (índice, elemento) para cada elemento na lista.
# for indice, elemento in enumerate(lista): Itera sobre cada índice e elemento na lista.
# if elemento == max(lista): Verifica se o elemento atual é igual ao máximo da lista.

menor = [indice for indice, elemento in enumerate(lista) if elemento == min(lista)]



# Imprime os resultados
print(f'O menor elemento é {min(lista)} e ele aparece nas posições: {menor}')
print(f'O maior elemento é {max(lista)} e ele aparece nas posições: {maior}')
