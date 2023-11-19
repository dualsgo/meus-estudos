# Curso Python #18 - Listas PARTE 2


"""RESUMO"""
# O YouTuber continua a série de vídeos sobre a linguagem de programação Python, detalhando listas.
# Reconhece a importância da prática e conhecimento prévio de conceitos de programação para entender listas.
# Agradece aos colaboradores e patrocinadores que tornaram possível a criação do conteúdo.
# Incentiva os espectadores a assistir a vídeos anteriores e a sessão de transmissão ao vivo sobre Python e listas.

# Discussão sobre um vídeo da World 3 playlist no YouTube.
# O vídeo é uma animação, e o apresentador pede um favor relacionado ao próximo vídeo.
# O próximo vídeo abordará um novo conceito, exercícios e soluções serão discutidos, mas não imediatamente.
# Os exercícios serão ajustados, a solução será fornecida e testada antes de avançar para o próximo tópico.
# O próximo vídeo se concentrará em dicionários, com a importância de entender esse conceito para o entendimento geral do curso.
# A explicação detalhada de uma técnica específica será fornecida, impactando todos os exercícios.
# Discussão sobre diferentes exercícios e como aplicar conhecimentos adquiridos a outros exercícios.
# Exemplos serão fornecidos para explicar como o conhecimento de um exercício pode ser aplicado a outros.

# Discussão da estrutura de listas em Python, abordando a criação, manipulação, e métodos como append, insert, pop, e remove.
# Demonstração de slicing e indexing em listas, diferenciação entre listas e tuplas, e incentivo à prática.

# Discussão aprofundada sobre listas em Python, incluindo criação, acesso, manipulação de elementos, e uso eficiente para tarefas relacionadas a dados.

# Tutorial sobre como trabalhar com listas em Python, incluindo a criação de listas, adição de itens, uso de variáveis, list comprehension e operações condicionais e de funções.

# Discussão de um programa Python que organiza dados em listas, permitindo aos usuários inserir conjuntos de números e organizá-los em uma única lista.
# Destaque para a importância do programa e como ele pode demonstrar a compreensão do programador de estruturas de dados e algoritmos.

# Criação de um programa para ajudar jogadores a fazer palpites para a Mega-Sena, envolvendo geração de números aleatórios e lógica mais complexa com listas aninhadas.

# Continuação da discussão sobre listas em Python, destacando que listas podem conter outras listas, criando uma estrutura multinível.
# Enfatiza a importância de entender o uso de listas sem depender de código pré-escrito.
# Incentivo à prática e prévia do próximo tópico, dicionários.

"""CONTEÚDO"""
# Comando para declarar uma lista
dados = list()
# Comando para adicionar um elemento a lista
dados.append('Pedro')
dados.append(25)
# Sobrescrever os valores de uma lista
dados[0] = 'João'
# Agora o elemento no índice 0 que era Pedro vale João

# Listas dentro de listas
pessoas = list()
pessoas.append(dados[:])  # Atribuindo uma cópia de outra lista
# Agora o elemento 0 da lista pessoas é a lista dados que possui 2 elementos
print(dados)
print(pessoas)

# Outra forma de declarar seria
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
# Exibir índices específicos lista[sublista][elemento]
print(pessoas[0][0])  # Exibe Pedro, que é o elemento no índice 0 na lista de índice 0
print(pessoas[1][1])  # Exibe 19, que é o elemento 1 na lista de índice 1
print(pessoas[2][0])  # Exibe João, que é o elemento 0 na lista de índice 2
print(pessoas[1])     # Exibe ['Maria', 19], que é a lista no índice 1

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste)    # Cria uma ligação. Assim, as alterações em uma ocorrem também na outra
galera.append(teste[:])  # Cria uma cópia. Assim as alterações em uma não afetam a outra
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

# Sublistas
grupo = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(grupo[2][1])

# Iterando sobre listas de listas
for pessoa in galera:
    print(f'Nome: {pessoa[0]}, idade: {pessoa[1]}')

# Coletando dados para uma lista de listas
time = []
membro = []
tmais = tmenos = 0
for c in range(3):
    membro.append(str(input('Nome: ')))
    membro.append(int(input('Idade: ')))
    time.append(membro[:])
    membro.clear()
print(time)

# Analisando a lista de listas
for p in time:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        tmais += 1
    else:
        tmenos += 1
        print(f'{p[0]} é menor de idade.')

print(f'Temos {tmais} maiores e {tmenos} menores de idade!')
