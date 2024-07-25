# MIMO - 13 - Bibliotecas e módulos
# 13.3 - Introdução ao NumPy

# Projetos da realidade tendem a usar dados em abundância, tornando as operações muito lentas. Imagine uma rede
# social.
# No
# início o número de usuário é pequeno, mas à medida que a rede cresce a lista de usuários torna-se muito longa.

# NumPy, abreviação de Numerical Python, é uma biblioteca que fornece funcionalidades para trabalhar com grandes quantidades de dados. NumPy é uma das bibliotecas mais populares para trabalhar com dados numéricos. NumPy fornece uma estrutura de dados chamada array, que é semelhante a uma lista, mas muito mais rápida. NumPy também fornece funções para operações matemáticas em arrays.

# É comum abreviar NumPy como np.
import numpy as np

# Numpy nos permite armazenar dados em arrays. Podemos criar um array a partir de uma lista usando a função array().
# array() aceita uma lista como parâmetro e retorna um array.

np_array = np.array([1, 2, 3, 4, 5])

# Vejamos, por exemplo, se quisermos adicionar 1 a cada elemento de uma lista.
print(np_array)  # [1 2 3 4 5]

# Com NumPy podemos fazer isso em uma única linha.
print(np_array + 1)  # [2 3 4 5 6]

# Sem ele teríamos que usar um loop for.

"""for i in range(len(np_array)): # iteramos sobre os índices da lista
  np_array[i] += 1  # adicionamos 1 a cada elemento"""

# Com np_array = np.array([1, 2, 3, 4, 5]) estamos transformando uma lista em um array. Podemos criar um array vazio usando a função empty().

# Podemos converter listas com todos os tipos de dados, desde que todos os elementos sejam do mesmo tipo.
# Tentar criar um array com tipos de dados diferentes resultará em um array com um único tipo de dados.

stock = np.array([10, 12, "25"])
print(stock)  # ['10' '12' '25']

# Usamos a indexação para acessar elementos de um array. A indexação funciona da mesma forma que as listas. Podemos usar um índice negativo para acessar elementos a partir do final do array.
print(stock[0])  # 10

# Para saber a composição de um array usamos a função size().
print(stock.size)  # 3
print(np.size(stock))  # 3

# NumPy fornece funções para criar arrays com valores padrão. Por exemplo, podemos criar um array com todos os valores iguais a 0 usando a função zeros(). Precisamos somente informar o tamanho do array como parâmetro.
print(np.zeros(5))  # [0. 0. 0. 0. 0.]

# zeros cria um array com valores de ponto flutuante. Podemos criar um array com valores inteiros usando a função zeros() e especificando o tipo de dados como int.

# Da mesma forma, podemos criar um array com todos os valores iguais a 1 usando a função ones().

# Se quisermos criar um array com valores diferentes, o método arange() cria um array com valores sequenciais. O array começa em zero. Precisamos informar o valor inicial, o valor final e o intervalo como parâmetros. O valor final não é incluído no array.
print(np.arange(1, 10, 2))  # [1 3 5 7 9]

# Se quisermos criar um array com valores aleatórios, podemos usar a função random(). Precisamos informar o tamanho do array como parâmetro.