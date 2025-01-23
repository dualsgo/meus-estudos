# MIMO - 14 - Erros e exceções
# 14.3 - Comunicando com uma API

# O que é uma API?
# Interfaces de programação de aplicativos, também conhecidas como API, facilitam a comunicação entre dois programas.
# APIs enviam requisições de um programa remetente para um programa receptor. Em seguida, elas enviam respostas do receptor para o programa remetente.

# Muitas coisas em nossa vida diária funcionam como uma API. Um exemplo é um garçom e a equipe da cozinha.

# Um garçom, como um programa remetente, envia um pedido para a cozinha. Então a cozinha, como um programa receptor, envia de volta a comida como uma resposta.

# Agora, de volta aos programas. O código abaixo envia uma solicitação GET para uma API. Você consegue adivinhar o que uma solicitação GET faz?

# Se tudo funcionar, devemos receber os dados junto com um código de status 200, nos informando que tudo correu bem.

# GET https://mimo.org.courses HTTP/1.1

# Isso mesmo! O código era para solicitarmos alguns dados. https://mimo.org/courses é a API que nos ajudou a obtê-los!

# Mas de onde a API obteve a informação? Lembre-se de que a API permite a comunicação entre 2 programas. Resposta: a API obteve a informação de um banco de dados.

# Para interagir com bancos de dados, precisamos escrever código. Uma API nos permite fazer isso de uma maneira mais simples.

# Mas você precisa usar o método correto para realizar ações. Para recuperar dados, usamos GET. O que você acha que usamos para inserir dados? Resposta: POST.

# Isso mesmo! Podemos inserir dados em um banco de dados usando requisições POST.

# Ao contrário das requisições GET, precisamos enviar um corpo com as informações para requisições POST. Complete a requisição abaixo.

# Quando trabalhamos com Python, usamos a biblioteca requests para criar requisições.

import requests 
 
response = requests.get("https://mimo.org/courses") 
data = response.json() 
print(data)

# Também podemos fazer requisições POST com a biblioteca requests.

import requests 
 
url = "https://mimo.org/users" 
 
data = { 
  "username": "test_user", 
  "name": "tester" 
} 
 
response = requests.post(url, json=data) 
print(response.json())

# Por que usar uma API?

# Agora que você sabe o que é uma API, por que devemos usá-la? Uma razão é que APIs podem nos ajudar a construir um sistema mais rapidamente.

# Desenvolvedores de back-end não precisam esperar que o desenvolvimento front-end seja concluído para testar seu programa.

# Eles podem testar seu programa simplesmente enviando requisições para a API e verificando se as respostas estão corretas.

# Já vimos as requisições GET e POST, mas ainda há as requisições DELETE, PUT e PATCH para aprender.

# As requisições DELETEdevem ter um identificador para informar à API o que deve ser deletado. Como o identificador 6 aqui.

# DELETE http://mimo.org/api/courses/6 HTTP/1.1

# Usamos o método delete para chamar um endpoint de exclusão usando requests.

import requests

url = "http://mimo.org/api/courses/1"

response = requests.delete(url)

# As requisições PUT são semelhantes às requisições POST, mas são usadas para substituir um objeto previamente criado.

# Como as requisições PUT são usadas para substituir objetos existentes, elas precisam de identificação para saber qual objeto substituir.

# Se uma identificação inválida ou nenhuma identificação for fornecida em uma solicitação PUT, um novo objeto será criado.

PUT https://mimo.org/users/1 HTTP/1.1

{
 "username": "test_User",
 "name": "tester"
}

# O código de status da resposta será 201 para objeto criado e 204 para objeto substituído. Codifique uma requisição PUT sem identificação.

# PUT https://mimo.org/users HTTP/1.1 
 
{ 
 "username": "test_User", 
 "name": "tester" 
}

# Ao usar uma requisição PUT, ela remove todos os dados existentes e insere os dados com base no corpo da requisição.

# Usamos o método put para chamar um endpoint put usando requests.

#   As requisições PATCH são usadas para atualizar alguns campos de um objeto, portanto, é necessário identificar qual objeto atualizar.

# Os valores de todos os campos não mencionados permanecerão inalterados. Use 1 como a identificação para a solicitação abaixo.