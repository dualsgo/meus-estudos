# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.1 - Definir operações

# Assim como listas, podemos obter o tamanho de um conjunto com a instrução len()
# Quando todos os elementos de um conjunto estão presentes em outro, dizemos que este é um subconjunto do outro.
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
pares = {0, 2, 4, 6, 8}

# Para verificar isso, usamos a instrução .issubset() com o conjunto que queremos verificar entre os parênteses

# .issubset() retorna True se o conjunto da esquerda for um subconjunto do da direita e False caso contráro

# Todos os elementos do conjunto nums estão no conjunto pares?
print(numeros.issubset(pares))
# Todos os elementos do conjunto pares estão no conjunto 'nums'?
print(pares.issubset(numeros))

# Podemos salvar o boolean fornecido em uma variável.

#

# Podemos juntar dois conjuntos usando a instrução .union()

pares = {0, 2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}

nums = impares.union(pares)
print(f'União: {nums}')
nums = pares.union(impares)
print(f'União: {nums}')

# .union() nos da um novo conjunto, sem duplicatas, mesmo que alguns elementos estejam em ambos os conjuntos originais.

# Da mesma forma, podemos criar um conjunto com os elementos que estão em ambos os conjuntos (interseção) com .intersection()

conjunto_a = {'a', 'e', 'i', 'o', 'u'}
conjunto_b = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
vogais = conjunto_a.intersection(conjunto_b)
print(f'Vogais: {vogais}')
vogais = conjunto_b.intersection(conjunto_a)
print(f'Vogais: {vogais}')

# Enquanto .union() nos fornece todos os elementos, .intersection() nos fornece apenas os elementos em comum.

# Podemos salvar os conjuntos dados por union() e intersection() em variáveis

#

# Para obter um conjunto de elementos que estão presentes em um conjunto, mas não em outro, utilizamos a instrução .difference()
# A instrução nos dá os elementos que o conjunto da esquerda tem, mas que o conjunto da direita não tem
conjunto_a = {'a', 'e', 'i', 'o', 'u'}
conjunto_b = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
print(f'Tem no a mas não no b: {conjunto_a.difference(conjunto_b)}')
print(f'Tem no b mas não no a: {conjunto_b.difference(conjunto_a)}')

# Como antes, podemos salvar esse resultado em uma variável se necessário
