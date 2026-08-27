# MIMO - 10 - Compreeensões de listas
# 10.4 - Indexação e exlusão negativa

# Python nos permite usar indexação negativa pra recuperar valores do final de um objeto indexável, como uma lista ou string.
scores = [4.5, 5, 3, 4, 3.5, 4]
#        [  0, 1, 2, 3,   4, 5]
#        [ -6,-5,-4,-3,  -2,-1]
latest = scores[-1] # 4
print(latest)

# A indexação negatiava significa que recuperamos um elemento do lado direito de uma lista. Usamos o símbolo de menos (-) antes do índice para indicar um índice negativo.
# Podemos usar qualquer valor negativo até o comprimento da lista, inclusive o que recuperaria o primeiro elemento, nesse caso -6.

# Com esse recurso, também podemos modificar elementos de uma lista começando pelo final.
# Encontraremos um erro se tentarmos recuperar um valor em uma posição fora do intervalo do comprimento da lista.

# As tuplas também são estruturas de dados ordenadas e os valores podem ser recuperados, mas são imutáveis, ou seja, não podem ser modificados.

# A palavra chave del nos permite excluir objetos ou itens de uma estrutura da dados
# Para excluir um elemento de uma lista, usamos a instrução del seguida do nome da lista e do índice do elemento entre colchetes.
del scores[0] # Exclui o primeiro elemento da lista
print(scores)   # [5, 3, 4, 3.5, 4] antes era [4.5, 5, 3, 4, 3.5, 4]
# del pode ser usado para exluir qualquer objeto, incluindo variáveis, tuplas, dicionários e conjuntos.

# Podemos usar del com uma chave dentro de um dicionário para excluir um par chave-valor indesejado do dicionário.

product = {
  'category': 'book',
  'price': 4.99,
  'in_shop': True}

del product['in_shop']
print(product) # {'category': 'book', 'price': 4.99}  