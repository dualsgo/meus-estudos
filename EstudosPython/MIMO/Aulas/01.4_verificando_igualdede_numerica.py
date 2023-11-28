# MIMO - 01 - Noções básicas de Python

# 01.4 - Verificando a igualdade numérica

# Operador de igualdade (==)

# Aprendemos a criar e armazenar valores, mas como compará-los? Como verificar se o PIN inserido de um usuário corresponde ao PIN salvo.

pin_inserido = 5448
pin_salvo = 5440

# Para comparar se dois números são iguais, usamos o operador de igualdade (==).
verificacao = pin_inserido == pin_salvo

# Ao comparar, há apenas dois resultados: True ou False
print(verificacao)

# Quando comparamos os mesmos números com o operador de igualdade, o resultado é True
# Quando comparamos os diferentes números com o operador de igualdade, o resultado é False.

# Operador de desigualdade (!=)

# Para verificar se um número não é igual a outro, usamos o operador de desigualdade (!=)

# Podemos armazenar o resultado de uma comparação com o operador de igualdade ou desigualdade em uma variável.

# Podemos comparar valores com variáveis e variáveis com outras variáveis com os operadores. 

primeiro = 1
segundo = 2
print(primeiro) # Exibe 1
print(segundo) # Exibe 2
print(primeiro != segundo) # Exibe False
