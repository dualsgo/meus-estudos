# MIMO - 10 - Compreeensões de listas
# 10.2 - Funções como expressões

# Podemos usar uma criação de listas para criar uma nova lusta, aplicando a função halve() a cada elemento de uma lista existnte, como prices
prices = [10, 22, 30, 40, 58, 62]

# A função que usaremos, halve(), pega um num como argumento e retorna sua metade com num/2
def halve(num):
    return num / 2

# Como antes, começamos iterando cada price na lista prices original com loop for
halved = [halve(price) for price in prices]

# Podemos escolher as operações que queremos aplicar a cada valor de price em uma função com halve() e usá-la como expressão.
# As funções são úteis quando queremos aplicar mais expressões, como retirar o imposto antes de reduzir o preço pela metade.

def halve(num):
    no_tax = 0.85 * num  # Remove 15% de imposto
    return no_tax / 2  # Retorna a metade do preço sem imposto

halved = [halve(price) for price in prices] 
print(halved)

# Só podemos usar funções que possume uma instrução return, pois na verdade estams anexando o valor retornado pela função à lista.