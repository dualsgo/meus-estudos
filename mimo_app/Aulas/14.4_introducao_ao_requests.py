# MIMO - 14 - Erros e exceções
# 14.4 - Introdução ao requests

# No desenvolvimento de software, interagir com serviços web é uma tarefa comum, frequentemente envolvendo o envio de requisições para servidores.

# A biblioteca Python requests simplifica o processo de fazer requisições.

# A biblioteca requests em Python é usada para fazer requisições HTTP para uma URL especificada.

# A biblioteca requests tornará simples, seja você tentando acessar os dados de um site ou interagir com um serviço web.

import requests

url = "https://rickandmorty.mimo.dev/api/character/1"
response = requests.get(url)
character_data = response.json()

print(f"Name: {character_data['name']}")
print(f"Status: {character_data['status']}")

# Para usar requests, temos que importá-lo usando a palavra-chave import, seguida pelo nome do pacote requests.

# Podemos então chamar requests.get() e passar uma URL para fazer uma solicitação HTTP GET.

# As requisições HTTP GET são o tipo mais comum de requisição usada na web, projetadas principalmente para recuperar dados de um determinado recurso.
 
url = "https://rickandmorty.mimo.dev/api/character/1" 
response = requests.get(url)

# A função get() retorna uma resposta que podemos salvar em uma variável. O objeto de resposta tem um código de status e dados ou um erro anexado.

# Para acessar os dados, precisamos analisar o objeto de resposta. Fazemos isso com .json(). Os dados analisados são um dicionário de chaves e valores.
 
url = "https://rickandmorty.mimo.dev/api/character/1" 
response = requests.get(url) 
data = response.json() 
 
print(data)

# Podemos acessar os valores como em qualquer outro dicionário com o qual trabalhamos.
 
url = "https://rickandmorty.mimo.dev/api/character/1" 
response = requests.get(url) 
data = response.json() 
 
print(data["name"]) 
print(data["status"])

# Trabalhar com web APIs envolve enviar e receber dados pela internet. Ao trabalhar com a resposta, precisamos garantir a integridade dos dados. É para isso que o status code é usado.

# O objeto de resposta tem um status_code associado a ele. Devemos verificar se é igual a 200 para garantir que os dados foram recuperados com sucesso.
 
url = "https://pokedex.mimo.dev/api/pokemon/pikachu" 
response = requests.get(url) 
 
if response.status_code == 200: 
  print("Data successfully retrieved") 
else: 
  print("Failed to retrieve data")
  
# Depois de garantir que os dados foram recuperados com sucesso, podemos descompactá-los.

url = "https://pokedex.mimo.dev/api/pokemon/pikachu"
response = requests.get(url)

if response.status_code == 200:
  print("Data successfully retrieved")

  pokemon_data = response.json()
  print(f"Name: {pokemon_data['name']}")
  print(f"ID: {pokemon_data['id']}")
else:
    print("Failed to retrieve data")
    
# Em alguns casos, não obteremos o que esperamos. Por exemplo, não existe um Pokémon com o nome Mimo. Devemos sempre verificar o status_code, e caso encontremos um erro, não mexemos nos dados.

# Em vez de comparar o código de status diretamente, podemos também colocar a chamada de request em um bloco try. Em seguida, adicionamos um bloco except para capturar erros potenciais. Aqui, pegamos o erro do objeto de erro e o usamos como error.

 
url = "https://pokedex.mimo.dev/api/pokemon/pikachu" 
try: 
  response = requests.get(url) 
  response.raise_for_status() 
  print("Data successfully retrieved") 
  pokemon_data = response.json() 
  print(f"Name: {pokemon_data['name']}") 
  print(f"ID: {pokemon_data['id']}")
  
except requests.HTTPError as error: 
  print(error)
  

# Devemos chamar raise_for_status no objeto de resposta para identificar erros que podemos então capturar através do bloco except.