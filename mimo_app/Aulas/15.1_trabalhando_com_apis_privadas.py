# MIMO - 15 - Trabalhando com APIS privadas

# 15.1 - Variáveis de Ambiente

# Variáveis de ambiente armazenam configurações importantes, como senhas ou chaves de acesso, fora do seu código, tornando-as mais fáceis e seguras de gerenciar.

# Variáveis de ambiente em Python permitem que você defina pares de chave-valor de forma segura para o seu código. Isso é muito útil para armazenar informações sensíveis.

import os

api_key = os.getenv("MY_API_KEY")
print(api_key)

# As variáveis de ambiente devem sempre ser armazenadas de forma segura para proteger informações sensíveis. Você nunca deve codificar suas chaves de API ou senhas; o exemplo a seguir é para fins educacionais para demonstrar sua estrutura.

environment_variables = {
  "API_KEY": "12345-abcde-67890-fghij-12345",
  "SECRET_KEY": "mysecretkey"
}

print(environment_variables)
print("Don't do the above! It's dangerous to expose sensitive information directly in your code!")

# Em vez de codificar informações sensíveis, usamos variáveis de ambiente definidas no ambiente de execução do código, mas não codificadas. Você pode acessar um conjunto no ambiente através de os.getenv.

api_key = os.getenv("MY_API_KEY")
print(api_key)

# Você precisará do módulo OS para recuperar variáveis de ambiente dentro do seu script Python.

# Você pode acessar variáveis de ambiente usando getenv e especificando a chave para os dados que deseja recuperar como parâmetro.

# os é um módulo poderoso. Com sua função getenv, podemos recuperar uma única variável de ambiente por vez se fornecermos a chave.

# Tradicionalmente, os desenvolvedores usavam arquivos .env para armazenar variáveis de ambiente. No entanto, ambientes de desenvolvimento mais modernos, como o Mimo, oferecem uma maneira mais amigável de configurar variáveis de ambiente.

# O arquivo .env é um arquivo de texto que contém pares de chave-valor em linhas separadas.

#API_KEY=12345-abcde-67890-fghij-12345
#SECRET_KEY=mysecretkey.

# Se você salvar suas variáveis de ambiente em um arquivo .env, você pode usar a biblioteca dotenv para carregá-las no seu ambiente. Uma vez carregados, você pode acessá-los usando os.getenv no seu código.

import dotenv # Para ler variáveis de um arquivo .env em Python, precisamos importar dotenv.
import os


# Após importar a biblioteca dotenv, podemos carregar o conteúdo do arquivo .env usando o método load_dotenv.

dotenv.load_dotenv()

# Depois de carregarmos o arquivo .env com o método load_dotenv, podemos acessar as variáveis nele com os.getenv.
api_key = os.getenv("API_KEY")
print(api_key)

# Quando você cria um projeto no Mimo, um ambiente de desenvolvimento moderno, você não precisa carregar o arquivo .env.

# Ao trabalhar com variáveis de ambiente em Python, existem várias maneiras de carregá-las e acessá-las, dependendo das suas necessidades. Já vimos o os.getenv, agora, vamos explorar o os.environ.

# Para acessar todas as variáveis de ambiente, usamos o dicionário os.environ. Cada variável de ambiente é armazenada neste dicionário.

import os

print(os.environ)

# Em sistemas modernos, como o Mimo, as variáveis de ambiente já estão configuradas. No entanto, se você usar seu próprio arquivo .env, terá que carregá-lo primeiro através do método load_dotenv.

# Assim como com os.getenv, você pode acessar uma variável de ambiente específica usando o dicionário os.environ.

api_key = os.environ["API_KEY"]
print(api_key)

# Lembre-se de que os.environ é um dicionário. Você pode usá-lo como qualquer outro dicionário.

api_key = os.environ["API_KEY"]

# Enquanto os.getenv é um método que retorna um valor.

secret_key = os.getenv("SECRET_KEY")

print(api_key)
print(secret_key)

# Vamos explorar erros comuns com variáveis de ambiente em Python e como lidar com eles de forma eficaz.

# Se consultarmos uma variável de ambiente inexistente usando os.getenv, o resultado será None. Se consultarmos uma variável de ambiente inexistente usando os.environ, isso gerará um KeyError porque a variável não existe.

api_key = os.environ["NON_EXISTENT_KEY"]
print(api_key)

# Você pode definir um valor padrão para uma variável de ambiente no código, mas nunca use uma chave privada para isso, a fim de garantir a segurança.

api_key = os.getenv("NON_EXISTENT_KEY", "default_value")