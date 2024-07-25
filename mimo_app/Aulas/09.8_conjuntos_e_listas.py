# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.8 - Conjuntos e listas

# Ao contrário dos conjuntos, listas permitem valores duplicados. Para eliminar duplicatas em uma lista, podemos transformá-la em um conjunto com a instrução set() contendo o nome da lista entre os parênteses.

lista = [1, 2, 2, 3, 4, 5, 5, 6]
print(lista)

# set() nos fornece um conjunto de valores exclusivos que podemos armazenar em uma variável
nova_lista = set(lista)
print(nova_lista)

# Podemos transformar o conjunto de volta em uma lista com a instrução list() contendo o nome do conjunto entre os parênteses.


