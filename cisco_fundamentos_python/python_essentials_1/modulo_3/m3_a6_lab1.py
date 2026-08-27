# 3.6.6 LAB Operações com listas ‒ básico
# Cenário

# Imagine uma lista - não muito longa, não muito complicada, apenas uma lista simples que contém alguns números inteiros. Alguns desses números podem ser repetidos, e essa é a pista. Não queremos repetições. Queremos que eles sejam removidos.
# Sua tarefa é escrever um programa que remova todas as repetições de números da lista. O objetivo é ter uma lista na qual todos os números não aparecem mais de uma vez.
# Nota: suponha que a lista de origem seja codificada dentro do código - você não precisa inseri-la no teclado. Claro, você pode melhorar o código e adicionar uma parte que possa conversar com o usuário e obter todos os dados dele.

# Dica: recomendamos que você crie uma nova lista como uma área de trabalho temporária. Você não precisa atualizar a lista no seu lugar original.
# Sua tarefa é escrever um programa que remova todas as repetições de números da lista. O objetivo é ter uma lista na qual todos os números não aparecem mais de uma vez.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list = list(set(my_list))
# set() cria um conjunto de elementos unicos
# list() converte o conjunto em uma lista
print("A lista com os elementos exclusivos aqui")
print(my_list)

# Outro exemplo:
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Compreensão de lista para criar uma nova lista com elementos únicos
unique_list = [num for num in my_list if my_list.count(num) == 1]
# a lista unique_list recebera (unique_list =) o num para cada num na lista my_list (num for num in my_List) se o número de vezes que o num aparece na lista for igual a 1 (.count(num) == 1)
print("A lista com os elementos exclusivos:")
print(unique_list)

# Observação: Conjuntos são estruturas de dados que não permitem elementos
# duplicados. São caracterizados por chaves {}. Embora dicionários também sejam caracterizados por chaves, eles possuem uma estrutura diferente. Dicionários são compostos por pares de chave e valor, enquanto conjuntos são compostos apenas por valores. Eles são usados ​​para armazenar elementos exclusivos. Esse método é muito mais eficiente, pois não precisa percorrer a lista para verificar se o elemento já existe, ele simplesmente não adiciona o elemento se ele já existir.