# MIMO - 10 - Compreeensões de listas
# 10.1 - Usando compreensões de listas

# Para criar uma lista como halved com base em outra como prices, precisamos primeiro criar uma lista vazia e, em seguida preenchê-la dentro de um loop

prices = [10, 38, 40, 58, 62]
halved = []
# Para cada preço na lista de preços, dividimos o preço por 2 e adicionamos o resultado à lista halved
for price in prices:
    half_price = price / 2
    halved.append(half_price)

print(halved)

# Podemos construir a mesma lista halved de antes, mas em uma linha, usando list comprehension
# A sintaxe é nova_lista = [expressão for elemento in lista_original]
# A expressão é o que queremos que cada elemento da nova lista tenha, como price / 2. Ela pode ser uma operação matemática, uma função ou qualquer outra coisa que queremos que cada elemento da nova lista tenha.

halved = [price / 2 for price in prices]  # Cria uma lista com os preços divididos por 2
print(halved)

# Como uma criação de listas retorna uma nova lista, começamos com colchetes. 

# Em seguida, escrevemos a expressão que queremos que cada elemento da lista tenha, price / 2. Depois disso, escrevemos a instrução for price in prices para dizer ao Python que queremos que ele execute a expressão para cada elemento da lista prices. As compreensões de listas usam loops for para iterar cada elemento da lista original.

# Como acontece com qualquer loop for, price é a variável que contém os elementos da lista um por um, enquanto prices é a lista a qual estamos fazendo o loop

# No início da criação de listas, escrevemos uma expressão para aplicar em cada elemento, como reduzir pela metade cada preço com price/2

# Ao atribuir uma criação de listas a uma variável, estamos na verdade atribuindo a lista criada pela compreensão de listas à variável

# Exemplo: Criar uma lista de códigos de voo com list comprehension
flights = ["1122", "5788", "0044"]
codes_a = ["BA" + flight for flight in flights]
# Exemplo: Criar uma lista de códigos de voo com o mesmo resultado do exemplo anterior
codes_b = []
for flight in flights:
    code = "BA" + flight
    codes_b.append(code)
# O resultado é o mesmo, mas a criação de listas é mais curta e fácil de ler
print(codes_a)
print(codes_b)