# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.3 - Retornando tuplas

# As tuplas são úteis porque nos permitem retornar vários valores de uma função.
# Para retornar uma tupla, codificamos os valores que desejamos retornar separados por vírgula

# Esta função retorna uma tupla com a maior e a menor pontuação de uma lista de pontuações
def get_scores_data(scores_list):
    # A função max() retorna o maior valor de uma lista e min() retorna o menor
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    # A tupla é retornada
    return  highest_score, lowest_score # (100, 5)

# Para armazenar uma tupla retornada por uma função, atribuímos o resultado da chamada de função a uma variável como data

scores = [30, 17, 80, 100, 90, 10, 30, 5] # Essa lista de pontuações é passada para a função
data = get_scores_data(scores) # A tupla retornada é armazenada em data
print(data)


