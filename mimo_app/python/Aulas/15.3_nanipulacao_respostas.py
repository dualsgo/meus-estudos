# MIMO - 15 - Trabalhando com APIS privadas

# 15.3 - Manipulação de respostas

# Fazer a chamada da API é apenas a primeira parte; você também precisa lidar adequadamente com a resposta, verificar o status e extrair os dados de que precisa.

# Ao fazer uma chamada de API, recebemos de volta um objeto de resposta que contém o código de status, os cabeçalhos e o conteúdo real que recebemos.

# Se imprimirmos o objeto de resposta, veremos o código de status. Cada objeto de resposta inclui um código de status indicando o resultado da solicitação.

# Nós acessamos o código de status usando response.status_code.

import requests

response = requests.get("https://pokedex.mimo.dev/api/pokemon/pikachu")
print(response.status_code)

# Um código de status 2xx indica uma solicitação bem-sucedida. Códigos específicos como 200 OK significam que a solicitação foi processada corretamente, enquanto 201 Created indica que um novo recurso foi criado com sucesso.

# Um código de status 4xx indica um erro do cliente, o que significa que a solicitação foi inválida ou não pode ser atendida. Exemplos incluem 400 Bad Request, 401 Unauthorized e 404 Not Found.

# Vamos explorar como trabalhar com dados JSON em respostas de API, um formato comum para troca de informações entre clientes e servidores. Já vimos o objeto de resposta; precisamos do mesmo para analisar e trabalhar com dados JSON retornados da API.

# Podemos descompactar os dados JSON desta resposta usando a função json. Ao trabalhar com uma API, muitas vezes é útil imprimir todos os dados da resposta para ver se recebemos o que esperamos.

import requests

response = requests.get("https://pokedex.mimo.dev/api/pokemon/pikachu")
data = response.json()
print(data)

# Em Python, os dados JSON são analisados em uma estrutura semelhante a um dicionário, permitindo que você acesse os valores usando chaves. Definimos a chave como uma string dentro de colchetes para acessar o valor correspondente no dicionário.

response = requests.get("https://pokedex.mimo.dev/api/pokemon/pikachu")
data = response.json()
print(data["name"])

# Desde que o dicionário tenha a chave que estamos usando, podemos acessar quantos campos quisermos.

# Ao trabalhar com dados JSON, às vezes o nível superior é um array, o que significa que toda a resposta é uma lista de objetos em vez de um único objeto.

response = requests.get("https://pokedex.mimo.dev/api/pokemon")
data = response.json()
print(data)

# Depois de desempacotar o array, você pode percorrer seus elementos ou acessar diretamente um item pelo seu índice.

response = requests.get("https://pokedex.mimo.dev/api/pokemon")
data = response.json()
for pokemon in data:
  print(f"Name: {pokemon['name']}, ID: {pokemon['id']}") 
  
# Você pode acessar diretamente os elementos usando seu índice se estiver trabalhando com um array como a estrutura de nível superior.

response = requests.get("https://pokedex.mimo.dev/api/pokemon")
data = response.json()
print(data[0])