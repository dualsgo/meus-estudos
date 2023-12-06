# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.2 - Criando tuplas
# Listas de tuplas
# Podemos armazenar tuplas em uma lista como qualquer outro valor. Consideramos que cada tula tem um valor e assim como qualquer valor, usamos vírgula para separá-los.

# Podemos usar uma tupla específica na lista usando o seu índice. Após acessar o índice, podemos salvar a tupla em uma variável.

# Podemos usar um loop para iterar uma lista de tuplas.

score = [('Mia', 75), ('Lee', 90)]
for user_score in score:
    print(f'Result: {user_score}')

# Tuplas vs Listas

# Vejamos as semelhanças e diferenças entre tuplas e listas:
event_tuple = ('Saturday', '21:00', 'Anna\'s birthday')
days_list = ['Saturday', 'Sunday']

# Da mesma forma que nas listas, podemos acessar os valores de uma tupla pelo seu índice
print(event_tuple[1])
print(days_list[1])

# A principal diferença é que, diferentemente das listas, não podemos atualizar, adicionar ou excluir valores de tuplas.
# Dizemos que as tuplas são imutáveis, pois tentar modificá-las resulta em erro.

# Como são imutáveis, nós usamos tuplas para armazenar informações que não devem ser modificadas
