# Curso Python #16 - Tuplas

"""RESUMO"""

# Introdução ao tópico do vídeo, que é sobre tuplas em Python.
# Destaque para a data original de gravação e a importância da revisão antes da postagem.
# Cobertura dos conceitos básicos de tuplas, incluindo exemplos de uso em programação Python.
# Orientação para espectadores novos na programação.

# Revisão de conceitos básicos de variáveis em Python, explicando como funcionam e sua relação com a memória.
# Introdução ao conceito de tipos de dados, determinando que tipo de dados pode ser armazenado em uma variável.
# Exemplo de variável "antech" representando um sanduíche, destacando a modificação e reatribuição de variáveis.
# Discussão sobre arrays multi-dimensionais e listas como estruturas de dados mais complexas.
# Explicação de que, embora Python use uma abordagem diferente para arrays multi-dimensionais, ainda é possível criar arrays e listas com várias dimensões.

# Discussão detalhada sobre o conceito de tuplas em Python.
# Cobertura da definição, sintaxe e limitações das tuplas.
# Explicação sobre como criar, manipular e indexar tuplas usando índices numéricos.
# Comparação entre tuplas e listas, abordando o tratamento de casos em que o índice está fora do intervalo.
# Exemplos e exercícios para ajudar os alunos a compreender os conceitos.

# Expansão para conceitos mais complexos em Python, abrangendo funções, bibliotecas e estruturas de dados como dicionários, listas e conjuntos.
# Revisão de todo o conteúdo aprendido desde o início da série.

# Início da parte prática do curso, incentivando os espectadores a praticarem o que aprenderam.

# Demonstração de como manipular tuplas, iterar sobre elas e acessar seus elementos.
# Correção de uma suposição errada sobre ignorar o último elemento de uma tupla ao iterar sobre ela.
# Exemplos de notação de fatia usando números negativos para acessar elementos do final da tupla.
# Demonstração da imutabilidade das tuplas e da mensagem de erro exibida ao tentar atribuir valores a um elemento da tupla.
# Exemplos de uso de loops "for" para iterar sobre tuplas e criar sub-tuplas.
# Uso de funções integradas como len() e id() para verificar o comprimento e a identidade de uma tupla.
# Uso de um dicionário para iterar e calcular a soma dos elementos de uma tupla.

# Discussão sobre o uso da estrutura de dados de tupla em Python, usando o exemplo de uma mercearia.
# Explicação de várias funcionalidades, como acessar elementos em ordem sequencial, fatiar tuplas e usar 'f-strings' para exibir a tupla.
# Técnicas de manipulação de elementos de tuplas, como alteração de elementos e adição de novos ou criação de outra tupla com um conjunto diferente de elementos.
# Exemplos envolvendo cenários de ficção científica e técnicas de web scraping, enfatizando a importância de acessar elementos em tuplas.

# Explicação sobre a funcionalidade de ordenar tuplas, referindo-se ao exemplo de um pedido de almoço.
# Destaque para a imutabilidade das tuplas e como a ordenação envolve reorganizar seus elementos.
# Explicação sobre a função integrada `sort()` e como ela pode ser usada para ordenar tuplas com base nos valores de seus elementos.
# Demonstração de como funções computacionais como `itermap()` e `imap()` podem ser usadas em conjunto com tuplas para obter resultados específicos.
# Exemplos de como colchetes podem ser usados para criar listas e atribuí-las a variáveis, permitindo a manipulação de tuplas usando métodos de lista.

# Descrição do comportamento de Python ao lidar com tuplas, destacando sua imutabilidade.
# Discussão de como acessar elementos dentro de uma tupla usando diferentes métodos, como indexação e fatiamento.
# Abordagem sobre como somar, filtrar e encontrar a primeira ocorrência de um valor específico dentro de uma tupla.

# Discussão sobre como as letras podem ser usadas como uma lista em Python.
# Exemplo de uso de letras para representar uma lista de times de futebol no Campeonato Brasileiro, ordenados alfabeticamente.
# Demonstração de como usar tuplas para armazenar uma lista de números aleatórios gerados usando o módulo random do Python.
# Explicação de como criar um loop que gera cinco números aleatórios e, em seguida, usa esses números para criar uma tupla com dois números aleatórios.
# Explicação sobre como classificar e ordenar uma lista de strings com base em critérios específicos e armazenar um dicionário de nomes e preços de produtos.

# Demonstração de como analisar uma palavra e identificar suas vogais usando Python.
# Início de um exercício que envolve identificar as vogais na palavra "aprender" e exibir a palavra decomposta em suas vogais individuais (a, e, e).
# Uso da palavra quebrada para criar uma lista de palavras e fornecer exercícios adicionais para aumentar a flexibilidade na programação Python.
# Explicação de várias instruções, como "tuple()", que são úteis no tratamento de tuplas.
# Incentivo para os espectadores concluírem os exercícios fornecidos, enfatizando que a conclusão é tão importante quanto o curso em si.
# Discussão sobre a importância de ser um bom programador e criar seus próprios programas, em vez de depender apenas da imitação.
# Incentivo aos espectadores para curtir e se inscrever no canal, com agradecimentos por suas contribuições para o curso.


"""CONTEÚDO"""
# Variáveis armazenam informações em espaços na memória
lanche = 'Hamburguer'
# Elas podem ser atualizadas, substituindo o valor anterior
lanche = 'Suco'
# Essas são variáveis simples

# Podemos usar variáveis compostas:
# Tuplas, Dicionários e Listas

# Declaramos as tuplas com parênteses (Mas nas versões mais atuais podemos omitir os parênteses
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Os elementos podem ser acessados por seus índices:
# Por exemplo, Hamburguer é o índice 0, Suco é 1, Pizza é 2 e Pudim é 3.

print(lanche)  # Exibe todos os valores
print(lanche[2])  # Exibe apenas o valor do índice 2, no caso, Pizza

# Tecnicamente, strings são variáveis compostas pois cada caractere recebe um índice
# Podemos acessar valores em um intervalo específico com o fatiamento. O último elemento é ignorado
print(lanche[0:2])

# Começa no índice 1 até o final
print(lanche[1:])
# Acessa o último elemento
print(lanche[-1])

# O método len() funciona e mostra a quantidade de elementos
print(len(lanche))  # Exibe 4

# Estrutura de repetição: Faz a iteração entre os elementos da tupla
for comida in lanche:
    print(comida)

# AS TUPLAS SÃO IMUTÁVEIS: Em Python não podemos modificar os elementos das Tuplas

# Iterando
for cont in range(0, len(lanche)):
    print(f'Eu vou comer: {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer: {comida}')

# Iterando e mostrando o contador
for cont in range(0, len(lanche)):
    print(f'{cont} - Eu vou comer: {lanche[cont]}')

for indice, comida in enumerate(lanche):
    print(f'{indice} - Eu vou comer: {comida}')

# Método sorted() mostra a tupla em ordem
print(sorted(lanche))
# Mas não altera o valor! Apenas exibe em forma de lista
print(lanche)

# Somando tuplas
tupla_a = (2, 5, 4)
tupla_b = (5, 8, 1, 2)
# Une os valores das tuplas mantendo a ordem
tupla_c = tupla_a + tupla_b
print(tupla_c)
# Mostra o comprimento da tupla
print(len(tupla_c))
# Mostra a quantidade de ocorrências - Nesse caso mostra duas ocorrências do dígito 2
print(tupla_c.count(2))

# Mostrar a posição de um determinado dígito. Havendo mais de um, mostra a primeira ocorrência
print(tupla_c.index(8))

# Em Python as tuplas aceitam valores de tipos diferentes
pessoa = ('String', 1, 2.5, True)
print(pessoa)
print(type(pessoa[0]))
print(type(pessoa[1]))
print(type(pessoa[2]))
print(type(pessoa[3]))

# Podemos deletar a tupla com o comando del()
del pessoa

