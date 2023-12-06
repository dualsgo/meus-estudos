# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.5 - Usando dicionários

# Acessando e atualizando valores

# Acessamos os valores do dicionário po sua chave - Codifique oo nome do dicionário e depois a chave entre colchetes
actor_bio = {
    'name': 'Bill Murray',
    'idade': '70'
}
print(actor_bio['name'])

# Após acessar um valor, podemos armazená-lo em uma variável

nome_ator = actor_bio['name']

# Podemos iterar através das chaves do dicionário com um loop for

player_scores = {
    'ann': 13,
    'michael': 20,
    'ava': 34
}

for player in player_scores:
    print(player_scores[player])

# A variável player representa as chaves, então podemos acessar o valor de cada chave usando player como o nome da chave

# Para atualizar um valor associado a uma chave nós acessamos o valor e atualizamos como faríamos com qualquer variável, codificando o operador de atribuição seguido do novo valor
print(player_scores)
player_scores['ann'] = 60
print(player_scores)

# Adicionando um par de valores-chave

# Para adicionar uam chave, codificamos o nome do dicionário e depois o nome da nova chave entre colchetes, seguido do operador de atribuição e o valor. O procedimento é semelhante a uma atualização, exceto pelo fato de que a chave não estava presente antes no dicionário.

player_scores['Maycon'] = 50
print(player_scores)

# Verificando e um dicionário contém uma chave

# Para verificar uma determinada chave, utilizamos o operador in
print('Douglas' in player_scores)

# Tal como acontece com as listas, o operador in nos dará True quando a chave estiver presente e False quando não. Podemos armazenar essa informação em uma variável.


# Removendo um par de chave-valor

# Removemos de forma semelhante a de um elemento de uma lista, codificando o nome do dicionário, seguido da instrução .pop()

# Precisamos especificar qual a chave queremos remover entre os parênteses
player_scores.pop('Maycon')
print(player_scores)

# Podemos armazenar o valor removido em uma variável

# Tentar remover um valor que não existe gera um erro. Para evitar isso, é boa prática ao remover chaves, verificar antes com o operador in se ela está presente no dicionário.

if 'Maycon' in player_scores:
    player_scores.pop('Maycon')
    print(player_scores)
else:
    player_scores['Maycon'] = 'Agora sim'
    print(player_scores)
