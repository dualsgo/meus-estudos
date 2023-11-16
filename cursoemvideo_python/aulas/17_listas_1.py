# Curso Python #17 - Listas

"""RESUMO"""

# Introdução ao conceito de listas em Python e comparação com tuplas.
# Enfatiza a mutabilidade das listas em comparação com a imutabilidade das tuplas.
# Agradece aos colaboradores e menciona o patrocinador do curso, Hostnet.

# Explicação das diferenças entre tuplas e listas em Python.
# Demonstração de como adicionar e remover elementos em listas.
# Uso dos métodos append, insert, del, pop, remove e do operador "in".
# Explicação clara e exemplos de como trabalhar com listas em Python.

# Destaque para a importância do operador range na criação de listas em Python.
# Uso do operador range para criar listas através da função "list" e por meio de intervalos numéricos.
# Demonstração dos métodos sort, reverse e da função len para manipular e obter informações sobre listas.
# Breve anúncio do site "estudonauta.com" oferecendo cursos de programação.

# Demonstração de como criar e manipular listas em Python.
# Ênfase na mutabilidade das listas e prática de operações como adição, remoção, ordenação e formatação.
# Incentivo à prática para compreensão profunda e teste do código em computadores pessoais.

# Discussão sobre como remover itens de uma lista usando um loop e a palavra-chave "in".
# Demonstração de como imprimir uma lista formatada usando um loop for e a palavra-chave "enumerate".
# Ênfase na importância dos testes e encorajamento para experimentar o código para compreensão total.
# Introdução à leitura de valores do teclado e adição a uma lista para uso posterior.
# Mostra uma peculiaridade do Python onde duas listas com os mesmos valores são consideradas iguais.

# Discussão sobre a criação e manipulação de listas em Python.
# Explicação sobre a criação de uma lista formatada e manipulação de valores.
# Aviso sobre a criação de uma ligação entre duas listas se uma for criada a partir da outra.
# Demonstração de como criar uma cópia de uma lista para evitar esse problema.
# Introdução de exercícios para praticar a manipulação de listas, incluindo encontrar os maiores e menores números em uma lista.

# Demonstração da implementação de dois exercícios em Python envolvendo listas.
# O primeiro envolve criar uma lista de valores únicos com base na entrada do usuário.
# O segundo requer a inserção de valores em uma lista na ordem correta sem usar ordenação.
# O terceiro envolve ler vários valores do usuário e exibir a lista de números em ordem decrescente, com informações sobre a presença do número 5.
# Todos os exercícios exigem o uso de comandos e lógica múltiplos.

# Apresentação de dois desafios para os espectadores.
# O primeiro desafio é criar um programa que lê uma lista de números e cria três listas separadas - uma para todos os números, uma para números pares e outra para números ímpares.
# O segundo desafio é criar um programa que verifica se uma expressão matemática dada possui parênteses correspondentes e retorna se é válida ou inválida.
# Os desafios são considerados difíceis, mas com prática, podem ser superados. Servem como revisão de lições passadas sobre loops e listas e como base para futuras lições.

# A seção não oferece informações úteis para resumo.

"""CONTEÚDO"""

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche[2]) # Exibe Pizza
# As estruturas das listas são muito parecidas com as tuplas, porém são mutáveis
lanche[2] = 'Coxinha'
print(lanche[2]) # Agora o valor Pizza é substituído

# As listas permitem adicionar valores: Usamos o método append('Valor'). Ele adiciona o valor ao último elemento

lanche.append('Coca-Cola')
print(lanche) # Agora exibirá 5 valores

# Os itens também podem ser adicionados em índices específicos com o método insert()

lanche.insert(0, 'Cachorro Quente')
print(lanche) # Agora irá exibir o Cachorro Quente no primeiro índice

# Para eliminar elementos temos o comando del

del lanche[3]
print(lanche)
# Também há o método pop() que remove o último elemento caso não receba um parâmetro

lanche.pop()
print(lanche)
# O método remove() recebe o valor a ser removido como parâmetro. Havendo mais de uma ocorrência, somente a primeira será removida

lanche.remove('Suco')
print(lanche)

# Ao tentar remover um elemento que não existe ocorerrá um erro. Podemos usar o comando if para verificar se o elemento está na lista. Com essa verificação, caso o elemento não exista evitamos o erro

# Podemos criar listas através de range() com o comando list()
from random import randint
valores = list(range(randint(4,11)))
print(valores)
# O método sort() ordena os valores
# Para ordem inversa usamos um parâmetro
valores.sort(reverse=True)
print(valores)

# O método len() também funciona para mostrar o comprimento da lista
len(valores)

# Iterando sobre listas
valores_2 = []
for contador in range(0, 5):
    valores_2.append(int(input(f'Digite o valor da posição {contador}: ')))
for posicao, valor in enumerate(valores_2):
    print(f'Na posição {posicao} encontrei o valor {valor}.')
print('Chegamos ao fim da lista!')

#

lista_a = [2, 3, 4, 7]
lista_b = lista_a # Ao igualar duas lista elas ficarão ligadas, não serão uma cópia da outra. Assim, qualquer alteração em uma repercute na outra
lista_b[2] = 8
print(f'LISTA A: {lista_a}') # Exibe 2, 3, 8, 7
print(f'LISTA B: {lista_b}') # Exibe 2, 3, 8, 7

# Para evitar isso podemos atribuir os valores de uma lista a outra assim:
lista_a = [2, 3, 4, 7]
lista_b = lista_a[:]
lista_b[2] = 8
print(f'LISTA A: {lista_a}') # Exibe 2, 3, 4, 7
print(f'LISTA B: {lista_b}') # Exibe 2, 3, 8, 7