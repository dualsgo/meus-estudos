# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.1 - Definir operações

# Assim como listas, podemos obter o tamanho de um conjunto com a instrução len()
# Quando todos os elementos de um conjunto estão presentes em outro, dizemos que este é um subconjunto do outro.
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # Todos os números
pares = {0, 2, 4, 6, 8} # Apenas os pares

# Para verificar isso, usamos a instrução .issubset() com o conjunto que queremos verificar entre os parênteses

# .issubset() retorna True se o conjunto da esquerda for um subconjunto do da direita e False caso contráro

# Todos os elementos do conjunto nums estão no conjunto pares?
print(numeros.issubset(pares)) # False - 1, 3, 5, 7, 9 não estão em pares
# Todos os elementos do conjunto pares estão no conjunto 'nums'?
print(pares.issubset(numeros)) # True - são eles: 0, 2, 4, 6, 8

# Podemos salvar o boolean fornecido em uma variável.

# Podemos usar a instrução .issuperset() para verificar se um conjunto contém todos os elementos de outro conjunto.
# .issuperset() retorna True se o conjunto da esquerda contiver todos os elementos do conjunto da direita e False caso contrário.

# Todos os elementos do conjunto nums estão no conjunto pares?
print(numeros.issuperset(pares)) # True - são eles: 0, 2, 4, 6, 8
# Todos os elementos do conjunto pares estão no conjunto 'nums'?
print(pares.issuperset(numeros)) # False - 1, 3, 5, 7, 9 não estão em pares

# Podemos juntar dois conjuntos usando a instrução .union()

pares = {0, 2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}
# .union() nos dá um novo conjunto com todos os elementos dos conjuntos originais
nums = impares.union(pares)
print(f'União: {nums}') # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# .union() nos da um novo conjunto, sem duplicatas, mesmo que alguns elementos estejam em ambos os conjuntos originais.
nums = pares.union(impares)
print(f'União: {nums}') # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Da mesma forma, podemos criar um conjunto com os elementos que estão em ambos os conjuntos (interseção) com .intersection()

conjunto_a = {'a', 'e', 'i', 'o', 'u'}
conjunto_b = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
# .intersection() nos dá um novo conjunto com os elementos que estão em ambos os conjuntos originais
vogais = conjunto_a.intersection(conjunto_b)
print(f'Vogais: {vogais}') # {'a', 'e'}

# .intersection() nos da um novo conjunto, sem duplicatas, mesmo que alguns elementos estejam em ambos os conjuntos originais.
vogais = conjunto_b.intersection(conjunto_a)
print(f'Vogais: {vogais}') # {'a', 'e'}

# Enquanto .union() nos fornece todos os elementos, .intersection() nos fornece apenas os elementos em comum.

# Podemos salvar os conjuntos dados por union() e intersection() em variáveis


# Para obter um conjunto de elementos que estão presentes em um conjunto, mas não em outro, utilizamos a instrução .difference()
# A instrução nos dá os elementos que o conjunto da esquerda tem, mas que o conjunto da direita não tem
conjunto_a = {'a', 'e', 'i', 'o', 'u'}
conjunto_b = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
# .difference() nos dá um novo conjunto com os elementos que estão no conjunto da esquerda, mas não no da direita
print(f'Tem no a mas não no b: {conjunto_a.difference(conjunto_b)}') # {'i', 'o', 'u'}
# .difference() nos da um novo conjunto, sem duplicatas, mesmo que alguns elementos estejam em ambos os conjuntos originais.
print(f'Tem no b mas não no a: {conjunto_b.difference(conjunto_a)}') # {'c', 'd', 'f', 'g', 'h', 'b'}

# Como antes, podemos salvar esse resultado em uma variável se necessário
