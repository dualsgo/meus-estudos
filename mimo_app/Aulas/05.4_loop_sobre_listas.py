# MIMO - 05 - Listas
# 05.4 - Loops sobre listas

# Existe uma maneira fácil de iterar por todos os elementos de lista usando um loop for
# Para isso, escrevemos fom uma variável de contador, a palavra in e o nome da lista
final_scores = [17, 22, 34, 13]
#    indices   [ 0,  1,  2,  3]           

# Para cada elemento da lista, o loop for executa o bloco de código
for score in final_scores:
    # A variável score contém o valor do elemento da lista em que o loop está atualmente e o exibe
    print(score)

# O loop será executado para tantos elementos quanto houver na lista.
# A variável antes de in contém o valor do elemento da lista em que o loop está atualmente.

# Se quisermos saber quantos elementos existem em uma lista, podemos usar a função len(). A sintaxe é: len(list)
print(len(final_scores)) # Retorna 4

# Durante a iteração, se quisermos saber o índice e valor do elemento atual, podemos usar a função enumerate(). A sintaxe é: enumerate(list)

# Podemos indicar o índice inicial da contagem com o argumento start. A sintaxe é: enumerate(list, start)
for indice, elemento in enumerate(final_scores, 10):  # O índice inicial da contagem é 10
    print(f'No índice {indice} está o valor {elemento}.')

# O argumento start é opcional. Se não for especificado, a contagem começa em 0. Ele não altera o índice da lista, apenas o valor do índice durante a iteração.

