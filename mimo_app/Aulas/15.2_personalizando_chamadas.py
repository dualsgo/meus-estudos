# MIMO - 15 - Trabalhando com APIS privadas

# 15.2 - Personalizando chamadas de APIs

# Vamos explorar como utilizar cabeçalhos e o corpo em requisições de API para enviar dados de forma segura e personalizar o comportamento das requisições.

# APIs frequentemente exigem que detalhes de autenticação sejam enviados através de cabeçalhos de API. Podemos especificar esses cabeçalhos ao fazer a solicitação de API.

import requests

headers = {"api-key": "MY_SECRET_KEY"}

requests.get("http://mimo.org/api/exclusive_guest_book", headers=headers)

# Os headers em uma solicitação de API são normalmente definidos como um dicionário, com cada chave representando o nome do header.

# Podemos passar diretamente o dicionário para o parâmetro headers sem salvá-lo em uma variável primeiro. No entanto, para a legibilidade, é melhor definir os headers separadamente, especialmente se eles forem complexos ou reutilizados em várias requisições.

headers = {"api-key": "MY_SECRET_KEY"}

requests.get("http://mimo.org/api/exclusive_guest_book", headers=headers)

# Para acessar uma API que requer autenticação, inclua as credenciais nos headers, ou o acesso será negado. No cabeçalho, normalmente adicionamos informações de autenticação, como chaves de API, tokens ou outros metadados necessários para a solicitação.

# Algumas APIs exigem que os dados sejam enviados no corpo da solicitação, além dos cabeçalhos. Nós os anexamos como json à chamada da API. No corpo, normalmente adicionamos os dados, como entrada do usuário, objetos JSON ou outro conteúdo a ser enviado para o servidor.

headers = {"api-key": "MY_SECRET_KEY"}
body = {"my-message": "I was here!"}

requests.post("http://mimo.org/api/exclusive_guest_book", headers=headers, json=body)

# Adicionar o header e o body faz parte da formação da solicitação da API. Dependendo do endpoint, devemos fornecer isso para garantir que o servidor entenda e processe nossa solicitação.

headers = {"api-key": "MY_SECRET_KEY"}
body = {"my-message": "I was here!"}

response = requests.post("http://mimo.org/api/exclusive_guest_book", headers=headers, json=body)
print(response.content)

# Os parâmetros de consulta são pares chave-valor adicionados a uma URL para enviar dados adicionais ao servidor, frequentemente usados para filtragem, ordenação, etc.

# Eles fazem parte da URL e especificam filtros ou opções, enquanto os headers e o corpo carregam metadados e dados.

# Para adicionar parâmetros de consulta à URL, você escreve um ponto de interrogação ? seguido pelo parâmetro de consulta. Após o ?, especificamos a chave, um sinal de igual =, e o valor.

url = "https://mimo.org/api/languages?popularity=high"

# Podemos também encadear múltiplos parâmetros de consulta juntos, separando-os com um &.

url = "https://mimo.org/api/languages?popularity=high&limit=1"

# Adicionar parâmetros de consulta é tedioso. Felizmente, podemos defini-los como um dicionário também. Um dicionário como este é muito mais simples de ler e manter.

import requests

params = {
  "popularity": "high",
  "limit": 1
}

# # Podemos passar o dicionário com os parâmetros de consulta como params para requests.get. Isso garante que a URL esteja formatada corretamente e torna o código mais limpo e fácil de manter.

import requests

params = {
  "popularity": "high",
  "limit": 1
}

response = requests.get("https://mimo.org/api/languages", params=params)
print(response.json())

# Por último, vamos trabalhar com paginação através de parâmetros de consulta. A paginação limita a quantidade de dados retornados para melhor legibilidade.

# import requests

params = {
  "page": 3
}

response = requests.get("https://mimo.org/api/exercises", params=params)
print(response.json())

