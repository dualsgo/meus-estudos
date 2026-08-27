# Trabalhando com APIs (Requests)

## EXPLICAÇÃO

APIs permitem que seu programa Python converse com outros serviços na internet (clima, banco de dados, redes sociais).

1. **Biblioteca `requests`**: A mais usada para fazer requisições HTTP.
2. **Métodos HTTP**:
   * **GET**: Recuperar dados (ex: ler um post).
   * **POST**: Enviar dados (ex: criar um usuário).
   * **PUT/PATCH**: Atualizar dados.
   * **DELETE**: Remover dados.
3. **JSON**: Formato padrão de troca de dados (em Python, vira um dicionário).
4. **Status Codes**: 
   * `200`: Sucesso.
   * `404`: Não encontrado.
   * `500`: Erro no servidor.

## EXEMPLO PRÁTICO

```python
import requests

# Exemplo de consulta (GET) em API pública (PokeAPI)
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

try:
    resposta = requests.get(url)
    
    # Verifica se a requisição deu certo (Status 200)
    if resposta.status_code == 200:
        dados = resposta.json() # Converte JSON para Dicionário
        print(f"Nome: {dados['name'].capitalize()}")
        print(f"Altura: {dados['height']}")
        print(f"Peso: {dados['weight']}")
    else:
        print(f"Erro na API: Status {resposta.status_code}")

except Exception as e:
    print(f"Erro de conexão: {e}")

# Exemplo conceitual de POST
# requests.post(url, json={"titulo": "Novo Post"})
```
