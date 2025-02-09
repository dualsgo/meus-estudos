# MIMO - 10 - Compreeensões de listas
# 10.5 - Notação de slice

# Às vezes queremos recuperar vários valores de uma lista. Podemos fazer isso usando slicing. Vejamos a sintaxe de slice: [start:stop:step]

ingredientes = ['eggs', 'flour', 'sugar', 'salt']
print(ingredientes[0:2]) # ['eggs', 'flour']

# O valor à esquerda dos dois pontos é a posição inicial do slice. Como abordamos anteriormente, a indexação do Python começa em zero

print(ingredientes[3:]) # ['salt']
# Ao codificar ingredinetes[3:], recuperamos todos os elementos da lista a partir da posição 3 até o final da lista.
# O valor inicial pode ser positivo, negativo ou omitido. Se omitido, o slice começa no início da lista. Valores negativos significam que o slice começa a partir do final da lista.

# Especificar um intervalo fora do comprimento da lista não causa um erro. Em vez disso, o slice retorna uma lista vazia.

# O valor à direita dos dois pontos é a posição final do slice. O slice inclui todos os elementos da posição inicial até a posição final, mas não inclui o elemento da posição final.
# Se usarmos um valor inicial de zero ou omitirmos o valor inicial, podemos omitir o primeiro dois pontos. Um valor de para da positivo será igual ao número de elementos retornados. 

# Um índice star maior que o índice stop resulta em uma lista vazia

# Também podemos usar um formato com dois dois pontos para especificar um valor de step. O valor de step é o número de elementos que o slice pula a cada iteração. O valor padrão de step é 1.

# Podemos usar um valor step sem valor start ou stop. Nesse caso, o slice começa no início da lista e vai até o final da lista, pulando o número de elementos especificado por step.
print(ingredientes[::2]) # ['eggs', 'sugar']

# step pode ser negativo, o que nos permite usar um valor start maior que o valor stop. Nesse caso, o slice começa no final da lista e vai até o início da lista, pulando o número de elementos especificado por step.
print(ingredientes[::-1]) # ['salt', 'sugar', 'flour', 'eggs']

scores = [100, 200, 300, 400, 500]
print(scores[0:2:-1]) # [] pois o step é negativo e o start é menor que o stop
print(scores[4:1:-1]) # [500, 400, 300] pois o step é negativo e o start é maior que o stop