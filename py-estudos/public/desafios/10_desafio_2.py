# MIMO - 10 - Compreeensões de listas - Desafio 1

# Você já percebeu como os navegadores adicionam automaticamente "https://" ao URL de um site? Vamos usar a criação de listas para adicionar "https://" à lista de sites em websites .

# Crie uma função add_https que use site como parâmetro. A função deve retornar "https://" adicionado ao parâmetro do site .
def add_https(site):
  return "https://" + site
# Após a função, crie uma variável auto_add que armazenará uma criação de listas.
websites = ["mimo.com", "coding.com", "food.org"]
auto_add = [add_https(website) for website in websites]
# A criação de listas deve percorrer cada item da lista websites .
# Codifique a expressão dentro da criação de listas que chama a função add_https nos itens da lista.
# Imprimir auto_add .
print(auto_add)
