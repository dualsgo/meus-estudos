# MIMO - 05 - Listas
# 05.3 - Atualizando  listas

# Vamos aprender como adicionar e remover valores de uma lista. Como neste app, que utiliza uma lista para gerenciar os dados de pontuação do usuário.

# Para adicionar o valor 25 a uma lista, codificamos o nome da lista seguido por um ponto e então a instrução append(). Sua sintaxe é: list.append(element)
scores = [24, 23]
print(scores)
scores.append(25)
print(scores)

# Adicionar um valor com append() o coloca no final da lista.

# Adicionamos um valor a um índice específico com insert(). Ao codificar insert(0, 33) adicionaremos o valor ao início da lista. A sintaxe é: list.insert(index, element)

# A função insert possui dois parâmetros. Primeiro, o índice onde queremos inserir o valor, seguido do valor.
(scores.insert(0, 33))
print(scores)

# Tanto append() quanto insert() só podem adicionar um elemento por vez.

# Para remover o último elemento de uma lista, codificamos o nome da lista, um ponto e a instrução pop()
scores.pop()
print(scores)

# Para remover um valor em um índice específico, adicionamos o índice que queremos remover entre parênteses, como pop(1)
removido = scores.pop(1)
print(scores)

# O valor removido também pode ser armazenado em uma variável.
print(removido)

# Para remover um elemento específico, usamos remove(). A sintaxe é: list.remove(element)
# scores.remove(24)

# Nesse caso, se o elemento não existir, o Python retornará um erro. Por isso é importante ter certeza de que o elemento existe antes de removê-lo.
# Podemos verificar antes se o elemento existe com o operador in.
# O operador in retorna True se o elemento existir na lista e False se não existir.
if 24 in scores:
    scores.remove(24)
else:
    print("O elemento não existe")
    
# Podemos utilizar o método clear() para remover todos os elementos de uma lista. A sintaxe é: list.clear()