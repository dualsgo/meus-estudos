# MIMO - 04 - Loops

# 4.2 - Loops while

# Os programas repetem as mesmas linhas de código continuamente para construir todo o tipo de coisas, como elementos repetidos de aplicativos.

# Uma maneira de repetir linhas de código é escrevê-las repetidamente, mas isso leva muito tempo se quisermos criar programas maiores.

# Para construir programas e sites maiores, repetimos linhas de código usando um loop while.

# Usar um loop while para repetir linhas de código começa com a palavra chave while.

# O loop while repete seu bloco de código enquanto sua condição e True

# O código que o loop while repete vem depois de :, detro do bloco de código recuado.

# Se a condição de um loop while permanecer True para sempre, nós o chamaremos de loop infinito.
verdade = True

while verdade:
    # O código dentro do loop while é repetido enquanto a condição for True
    print('Repita') # Repetimos o comando print() com a string 'Repita' enquanto a condição for True
    # Se não mudarmos a condição, o loop while será infinito e nunca terminará
    verdade = False  # Mudamos a condição para False para que o loop while termine

# Podemos usar um loop while para repetir linhas de código um número específico de vezes.
quantidade = 1  # Definimos uma variável quantidade com valor 0 ou seja, quantidade = 0 (ou a quantidade de vezes que queremos repetir o loop while)

while quantidade <= 10:
    # O código dentro do loop while é repetido enquanto a condição for True. Nesse caso, enquanto quantidade for menor que 10
    print(f'{quantidade} - Adicionando')   # Repetimos o comando print() com a string 'Adicionando' enquanto a condição for True
    quantidade += 1  # Adicionamos 1 ao contador para atualizá-lo a cada repetição do loop