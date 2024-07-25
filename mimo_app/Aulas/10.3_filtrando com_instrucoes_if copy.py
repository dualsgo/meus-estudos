# MIMO - 10 - Compreeensões de listas
# 10.3 - Filtrando com instruções if

# Podemos usar list comprehesion para criar uma nova lista filtrando elementos de uma lista existente, como criar uma lista de high_scores com valores maiores que 20

scores = [12, 47, 30,  29, 19, 35] # Lista de pontuações
# Ao usar uma condicional, a ordem usual é começar com a expressão, seguida pela instrução for e, em seguida, pela instrução if
# A sintaxe é nova_lista = [expressão for elemento in lista_original if condição]
# Começamos como de costume com um loop for para itrarar cada elemento da lista original como cada score em scores
# Para copiar cada elemento na nova lista, escrevemos score como nossa expressão, sem aplicar nenhuma operação
# Para filtrar elementos qie atendam a uma determinada condição, adicionamos uma comdição if, como aqui onde apenas copiamos a pontuação se ela for maior que 20 com if score > 20
high_scores = [score for score in scores if score > 20] # Lista de pontuações maiores que 20

high_scores.sort() # Ordena a lista
print(high_scores) # [29, 30, 35, 47]