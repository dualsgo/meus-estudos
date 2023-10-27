# MIMO - Listas

# Listas são coleções de dados. Os valores dentro de uma lista são chamados de elementos.
lista = [0, 1, 2, 3]  # Usamos vírgulas para separar os valores.

# Cada elemento da lista possui uma posição numerada chamada índice. Os índices começam em zero e aumentam para cada valor adicional. Podemos atualizar os valores dos elementos acessando seu índice.

# Para acessar um valor específico, usamos o nome da lista seguido do índice entre colchetes.
# Exibe o valor 3, que está no índice 3.
print(f"Valor no índice 3: {lista[3]}")

# Para alterar um valor, basta atribuir um novo valor à variável usando o índice.
lista[3] = 10
# Agora exibirá o valor 10, que está no índice 3.
print(f"Novo valor no índice 3: {lista[3]}")
print(f"Lista atualizada: {lista}")  # Podemos verificar a lista atualizada.

# Adicionando elementos a listas

# append(): Adiciona valores ao final da lista.
exemplo = [1, 12, 25, 19]
exemplo.append(90)
# Agora, o valor 90 será exibido após o valor 19.
print(f"Lista após o append(90): {exemplo}")

# insert(): Adiciona um valor em um índice específico.
# Suponha que a lista seja [1, 12, 25, 19, 90]
exemplo.insert(0, 36)  # Insere o valor 36 no índice 0.

# Agora todos os valores subsequentes mudaram seus índices devido à inserção.
print(f"Lista após o insert(0, 36): {exemplo}")

# Removendo elementos

# pop(): Remove o elemento no último índice da lista. Se quisermos eliminar um elemento específico, indicamos o índice como parâmetro.

# Podemos armazenar o valor removido em uma variável.
# Vamos remover o elemento que adicionamos anteriormente.
valor_removido = exemplo.pop(0)
print(f"Lista após o pop(0): {exemplo}")
print(f"Valor removido: {valor_removido}")

# Iterando através de elementos
lista = [0, 1, 2]

for item_lista in lista:
    print(f"Elemento da lista: {item_lista}")

# Contando elementos

# Usamos a instrução len(lista) para obter o número de elementos de uma lista.
print(f"Comprimento da lista: {len(exemplo)}")
comprimento = len(exemplo)
print(f"Comprimento armazenado em uma variável: {comprimento}")

# Listas vazias (lista[]) retornam zero. Podemos usar o comprimento da lista em instruções condicionais, por exemplo.

# Listando operações min() e max()

# Às vezes, é útil encontrar os valores mínimo e máximo de uma lista. Para isso, usamos as instruções min() e max().
print(f"Valor mínimo na lista: {min(lista)}")
print(f"Valor máximo na lista: {max(lista)}")

# Classificando dados com sort()

# Para classificar uma lista em ordem crescente, usamos a instrução .sort(). Isso altera a lista diretamente.
exemplo.sort()
print(f"Lista ordenada: {exemplo}")

# Soma de elementos com sum()
# Usamos a instrução sum() para encontrar a soma dos valores de uma lista.
# Podemos salvar o valor em uma variável se precisarmos usá-lo posteriormente.
total = sum(exemplo)
print(f"Soma dos elementos da lista: {total}")

# Combinando dados

# Para combinar dados de dois conjuntos ou mais, criamos uma expressão contendo os nomes das listas e o operador de adição +.
lista1 = [0, 1, 2, 3]
lista2 = [4, 5, 6, 7, 8, 9]
print(lista1 + lista2)
# O resultado é [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Ao usar +, a primeira lista será exibida seguida das demais, nessa ordem.
# Os dados das listas podem ser diferentes!

# Controlando a frequência

# Às vezes, queremos saber quantas vezes um dado está presente em uma lista.
# Usamos a instrução .count() após o nome da lista e colocamos o dado que desejamos consultar entre os parênteses.
uniao = lista1 + lista2
print(uniao.count(2))  # Verificando quantas ocorrências tem o número 2
# O resultado é 1

# Se não quisermos saber a quantidade de ocorrências, mas sim verificar se existe esse dado na lista, usamos in. Ele retorna um booleano.
print(10 in uniao)  # Consultando se existe o número 10 na lista
# O resultado é False
