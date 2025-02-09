# MIMO - 10 - Compreeensões de listas - Desafio 3

# Os sites de filmes recomendam filmes com base em classificações, popularidade, opções personalizadas, etc. Vamos usar a compreensão de lista para recomendar filmes com classificação superior a 4.

# Codifique uma criação de listas e atribua-a à variável recommended.
# A criação de listas deve percorrer cada item da lista ratings.
# Codifique a expressão dentro da criação de listas para verificar se a classificação é maior que 4. O resultado deve ser uma lista de valores booleanos.

ratings = [4.3, 3.1, 5, 1.1]

recommended = [rating > 4 for rating in ratings]

print(recommended)