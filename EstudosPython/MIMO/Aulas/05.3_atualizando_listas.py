# MIMO - 05 - Listas
# 05.3 - Atualizando  listas

# Vamos aprender como adicionar e remover valores de uma lista. Como neste app, que utiliza uma lista para gerenciar os dados de pontuação do usuário.

# Para adicionar o valor 25 a uma lista, codificamos o nome da lista seguido por um ponto e então a instrução append()
scores = [24, 23]
print(scores)
scores.append(25)
print(scores)

# Adicionar um valor com append o coloca no final da lista.

# Adicionamos um valor a um índice específico com insert(). Ao codificar insert(0, 33) adicionaremos o valor ao início da lista.
(scores.insert(0, 33))
print(scores)

# A função insert possui dois parâmetros. Primeiro, o índice onde queremos inserir o valor, seguido do valor.

# Tanto append() quanto insert() só podem adicionar um elemento por vez.

# Para remover o último elemento de uma lista, codificamos o nome da lista, um ponto e a instrução pop()
scores.pop()
print(scores)

# Para remover um valor em um índice específico, adicionamos o índice que queremos remover entre parênteses, como pop(1)
removido = scores.pop(1)
print(scores)

# O valor removido também pode ser armazenado em uma variável.
print(removido)