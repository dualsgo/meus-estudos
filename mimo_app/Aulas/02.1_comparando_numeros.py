# MIMO - 02 - Tipos e comparações

# 02.1 - Comparando números - Operadores de comparação

# Podemos usar comparações para verificar se um número é menor ou maior que outro número.

# Para isso utilizamos os operadores < (menor que) e > (maior que) que retornam True ou False.

print(1 < 10)  # Se o número da esquerda for menor que o da direita, o resultado será True.
print(10 < 1)  # Se o número da esquerda não for menor que o da direita, o resultado será False.

print(1 > 10)  # Se o número da esquerda não for maior que o da direita, o resultado será False.
print(10 > 1)  # Se o número da esquerda for maior que o da direita, o resultado será True.


# Caso os números sejam iguais retornará False em todos os casos!
print(1 > 1) # False
print(1 < 1) # False

# Verificando a igualdade
# Para verificar se um número é menor ou igual ou se é menor ou igual a outro, usamos os operadores <= ou >=
print(1 >= 1) # True
print(1 <= 1) # True

menor_valor = 1
maior_valor = 11
resultado = menor_valor <= maior_valor  # Assim como podemos comparar variáveis umas com as outras.
print(resultado)  # Podemos armazenar o resultado das comparações em variáveis.

