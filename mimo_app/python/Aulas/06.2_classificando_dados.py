# MIMO - 06 - Operações com listas
# 06.2 - Classificando dados

# As listas classificadas são úteis quando queremos entender a posição dos pontos de dados individuais, como pontuações, em relação aos outros.
pontos = [10, 11, 4, 15, 11, 7]
print(pontos)

# Para classificar uma lista como pontos, codificamos o nome da lista, um ponto e em seguida sort()
pontos.sort()
print(pontos)

# Ao usar sort() numa lista de números, os números são classificados em ordem crescente, sejam eles inteiros ou de ponto flutuante, negativos ou positivos.

# Ao usar sort() em uma lista de com strings, os valores são ordenados em ordem alfabética

# Se quisermos uma lista classificada em ordem decrescente, podemos usar o argumento reverse=True
pontos.sort(reverse=True)
