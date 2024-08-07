# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.7 - Criando conjuntos

# Quando queremos ter certeza de que uma coleção de valores não pode ter duplicatas, nós a armazenamos em um set. Conjuntos são coleções de valores como listas, mas não permitem valores duplicados.

# Para criar um conjunto, começamos com chaves para circundar os valores. Separamos os valores com vírgula e para reutilizar o conjunto, podemos armazená-lo em uma variável.

postcodes = {'SW1A', 'SY3', 'B44'}

# Podemos usar um loop para iterar um conjunto.
# Como os conjuntos não têm ordem, não podemos acessar valores por índice.
# A cada iteração, o loop acessa um valor diferente do conjunto.
print(postcodes)

