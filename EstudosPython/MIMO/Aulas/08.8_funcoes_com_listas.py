# MIMO - 08 - Funções
# 08.8 - Funções com listas

# Listas como argumentos

# Qualquer tipo de valor pode servir como entrada ou saída de uma função. Vejamos as funções podem usar listas como players

def is_multiplayer(players):
    return len(players) == 2
players = ['Amy', 'Jay']
print(is_multiplayer(players))

# Passamos listas para funções assim como fazemos com qualquer outro valor: codificando um nome de lista entre os parênteses da função.

# Após passarmos a lista para a função, podemos usar o parâmetro para exibi-la.

# Lembre-se de que os parâmetros são como variáveis que armazenam os valores que passamos para uma função.

# Aqui o parâmetro filmes irá armazenar os elementos da lista_filmes
def display_programme(filmes):
    print('Filmes disponíveis: ')
    print(filmes)

lista_filmes = ['Alien', 'Moon']
lista_tarefas = ['Fazer popoca', 'Lavar a louça']
# já que é com esse valor que chamamos a função.
display_programme(lista_filmes)

# Se mudarmos o valor
display_programme(lista_tarefas)

# Dentro da função, podemos usar todas as operações de listas, como len() para obter o número de passageiros

def contagem_passageiros(passageiros):
    return len(passageiros)

lista_passageiros = ['Ana', 'Juan', 'Cláudia', 'Fátima']
print(f'Temos {contagem_passageiros(lista_passageiros)} passageiros')

# A função pode usar o cumprimento da lista para comparações

# Às vezes queremos que nossa função recupere certos elementos de uma lista.
def get_vencedor(competidores):
    vencedor = competidores[0]
    print(f'O vencedor foi: {vencedor}')

competidores = ['Jay', 'Meg', 'Cy']
get_vencedor(competidores)

# As funções também podem atualizar listas, como atualizar o nome em tabela[0] para aquele no parâmetro time

def mudar_lider(tabela, time):
    tabela[0] = time
    return tabela

tabela = ['Botafogo', 'Palmeiras', 'Atlético', 'Flamengo', 'Gremio']
print(tabela)

tabela = mudar_lider(tabela, 'Vasco')
print(tabela)