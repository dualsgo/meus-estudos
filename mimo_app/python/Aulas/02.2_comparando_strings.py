# MIMO - 02 - Tipos e comparações

# 02.2 - Comparando strings

# Podemos usar comparações para verificar se uma string é igual ou diferente de outra string.

# Para verificar se uma string é igual a outra, utilizamos o operador de igualdade (==).
# Se a string da esquerda for igual à string da direita o resultado é True. Se não, o resultado e False.
print('online' == 'online')  # True
print('online' == 'ONLINE')  # False - Pois as letras maiúsculas e minúsculas são diferentes.

# Para verificar se uma string não é igual (ou diferente) de outra, utilizamos o operador de desigualdade (!=)
# Se a string da esquerda for diferente da string da direita, o resultado é True. Se não, o resultado é False.
print('online' != 'offline')  # True
print('online' != 'online')  # False
print('online' != 'ONLINE')  # True

# Também podemos comparar variáveis que armazenam strings entre sí.
fruta_1 = 'Maçã'
fruta_2 = 'Laranja'
print(fruta_1 == fruta_2)  # False
print(fruta_1 != fruta_2)  # True