# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.3 - Retornando tuplas

# As tuplas são úteis porque nos permitem retornar vários valores de uma função.
# Para retornar uma tupla, codificamos os valores que desejamos retornar separados por vírgula

def get_scores_data(scores_list):
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    return  highest_score, lowest_score

# Para armazenar uma tupla retornada por uma função, atribuímos o resultado da chamada de função a uma variável como data

scores = [30, 17, 80]
data = get_scores_data(scores)
print(data)


