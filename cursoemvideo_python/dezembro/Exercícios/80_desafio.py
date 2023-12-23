# Exercício Python #080 - Lista ordenada sem repetições - Aula 00 até 17 - Mundo 3
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

from random import randint

# Inicializa uma lista vazia para armazenar números em ordem crescente
numeros_ordenados = []

# Loop para gerar cinco números aleatórios e adicioná-los à lista em ordem crescente
for _ in range(0, 5):
    # Gera um número aleatório entre 0 e 9
    novo_numero = randint(0, 99)

    # Verifica se a lista está vazia ou se o número gerado é maior que o último elemento da lista
    if not numeros_ordenados or novo_numero > numeros_ordenados[-1]:
        # Adiciona o número ao final da lista
        numeros_ordenados.append(novo_numero)
        print(f'Número {novo_numero} adicionado ao final da lista.')
    else:
        # Inicializa a posição na lista
        posicao = 0

        # Loop para encontrar a posição correta do novo número na lista
        while posicao < len(numeros_ordenados):
            # Verifica se o novo número é menor ou igual ao elemento na posição atual
            if novo_numero <= numeros_ordenados[posicao]:
                # Insere o novo número na posição adequada e imprime a mensagem
                numeros_ordenados.insert(posicao, novo_numero)
                print(f'Número {novo_numero} adicionado na posição {posicao} da lista.')
                break
            posicao += 1

# Imprime a lista final com os números em ordem crescente
print(f'Os números gerados em ordem foram: {numeros_ordenados}')




