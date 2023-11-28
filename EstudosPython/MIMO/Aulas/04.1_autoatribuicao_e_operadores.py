# MIMO - 04 - Loops

# 4.1 - Autoatribuição e operadores
# Vamos aprender um novo conceito que explica como as variáveis controlam as coisas como adicionar ou retirar dólares de uma carteira.

# Quando criamos uma variável, atribuímos um valor a ela, como atribuir 3 a carteira
carteira = 3

# Autoatibuição é quando definimos uma variável com seu próprio valor. Por exemplo, podemos definir carteira com valor 3 com
carteira = carteira

# Como podemos autoatribuir variáveis, podemos aumentar ou diminuir variáveis definidas com números.
carteira = carteira + 1

# Variáveis autoatribuídas nos permitem rastrear dados que mudam ao longo do tempo.
carteira = 3
carteira = carteira + 2 # 3 + 2 = 5
carteira = carteira - 1 # 5 - 1 = 4
print(carteira)

# Variáveis definidas com strings funcionam da mesma forma.
nome = 'Nome na conta: '
nome = nome + 'Maycon'
nome = nome + ' Douglas.'
print(nome)

# Como a autoatribuição é uma ferramenta poderosa para criar programas, vamos aprender alguns operadores que nos ajudam a escrever código com mais rapidez.

# Sabemos que podemos adicionar 1 a uma variável escrevendo o nome da variável.
likes = 5
likes = likes + 1
print(likes)

# Em vez de escrever o nome da variável, podemos usar o operador += para adicionar um número com likes += 1
likes = 5
likes += 1
print(likes)

# Para subtrair do valor de uma variável, usamos -=