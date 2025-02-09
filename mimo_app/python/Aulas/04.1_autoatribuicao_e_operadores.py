# MIMO - 04 - Loops

# 4.1 - Autoatribuição e operadores
# Vamos aprender um novo conceito que explica como as variáveis controlam as coisas como adicionar ou retirar reais de uma carteira.

# carteira = carteira # carteira não existe, então não podemos atribuir um valor a ela

# Quando criamos uma variável, atribuímos um valor a ela, como atribuir 3 a carteira
carteira = 3
print(f'carteira = 3: {carteira}')

# Autoatibuição é quando definimos uma variável com seu próprio valor. Por exemplo, podemos definir carteira com valor 3 com
carteira = carteira  # agora carteira existe, então podemos atribuir um valor a ela
print(f'carteira = carteira: {carteira}')

# Como podemos autoatribuir variáveis, podemos aumentar ou diminuir variáveis definidas com números.
carteira = carteira + 1  # 3 + 1 = 4
print(f'carteira + 1: {carteira}')

carteira = carteira + 1  # 4 + 1 = 5
print(f'carteira + 1: {carteira}')

# Variáveis autoatribuídas nos permitem rastrear dados que mudam ao longo do tempo.
carteira = 3
carteira = carteira + 2  # 3 + 2 = 5
carteira = carteira - 1  # 5 - 1 = 4
print(carteira)

# Variáveis definidas com strings funcionam da mesma forma.
titulo = 'Senhor: '
nome = titulo + 'Maycon'
nome = nome + ' Douglas.'
print(nome)

# Como a autoatribuição é uma ferramenta poderosa para criar programas, vamos aprender alguns operadores que nos ajudam a escrever código com mais rapidez.

# Sabemos que podemos adicionar 1 a uma variável escrevendo o nome da variável.
likes = 5
likes = likes + 1 # 5 + 1 = 6
print(likes)

# Em vez de escrever o nome da variável, podemos usar o operador += para adicionar um número com likes += 1
likes = 5
likes += 1  # é o mesmo que likes = likes + 1
print(likes)

# Para subtrair do valor de uma variável, usamos -=
likes -= 1  # é o mesmo que likes = likes - 1 
print(likes)
