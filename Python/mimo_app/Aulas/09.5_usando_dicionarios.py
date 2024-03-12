# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.5 - Usando dicionários

# Acessando e atualizando valores

# Acessamos os valores do dicionário por sua chave
actor_bio = {
    'name': 'Bill Murray',
    'idade': '70'
}
# Codifique o nome do dicionário e depois a chave entre colchetes
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

# Podemos iterar pelas chaves, valores ou ambos

# Para iterar pelas chaves, usamos o método .keys()
print('Iterando pelas chaves')
for player in player_scores.keys():
    print(player)

# Para iterar pelos valores, usamos o método .values()
print('Iterando pelos valores')
for score in player_scores.values():
    print(score)

# Para iterar pelos pares de valores-chave, usamos o método .items()
print('Iterando pelos pares de valores-chave')
for player, score in player_scores.items():
    print(f'{player} - {score}')
    
# Para atualizar um valor associado a uma chave nós acessamos o valor e atualizamos como faríamos com qualquer variável, codificando o operador de atribuição seguido do novo valor
print(player_scores)
player_scores['ann'] = 60
print(player_scores)

# Adicionando um par de valores-chave

# Para adicionar uma chave, codificamos o nome do dicionário e depois o nome da nova chave entre colchetes, seguido do operador de atribuição e o valor. O procedimento é semelhante a uma atualização, exceto pelo fato de que a chave não estava presente antes no dicionário.

player_scores['Maycon'] = 50
print(player_scores)

# Verificando se um dicionário contém uma chave

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

# Dicionários aninhados
# Podemos armazenar dicionários dentro de dicionários. Isso é chamado de aninhamento.
dicionario_aninhado = {
    'brasil': {'cidade': 'São Paulo'},
    'usa': {'cidade': 'New York'}}

# Para acessar um valor aninhado, codificamos o nome do dicionário, seguido da chave do dicionário aninhado, seguido da chave do valor que queremos acessar
print(dicionario_aninhado['brasil']['cidade'])


# Se o dicionário possuir chaves repetidas, o Python irá sobrescrever o valor da chave repetida com o último valor encontrado. 

# Se quiser colocar 3 cidades em cada pais
dicionario_aninhado = {
    'brasil': {'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']},
    'usa': {'cidade': ['New York', 'Los Angeles', 'Chicago']}}

# Se quisermos iterar por um dicionário aninhado, podemos usar dois loops for
for pais in dicionario_aninhado:
    print(f'\n{pais.upper()}:')
    for cidade in dicionario_aninhado[pais]['cidade']:
        print(cidade, end=', ')        