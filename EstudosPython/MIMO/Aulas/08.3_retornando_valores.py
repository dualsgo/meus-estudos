# MIMO - 08 - Funções
# 08.2 - Criando parâmetros

# Às vezes, as funções precisam de informações específicas para ajudá-las a executar suas tarefas.

# Para começar, podemos usar variáveis dentro de funções.
def ola_ron():
    nome = 'Ron'
    print(f'Olá, {nome}')
ola_ron()
def ola_leslie():
    nome = 'Leslie'
    print(f'Olá, {nome}')
ola_leslie()

# Em vez diss podemos passar a informação apenas uma vez, sem repetir o código.
# Para passar o valor para uma função, primeiro adicionamos uam variável chamada parâmetro entre os parênteses
def ola_nome(nome):
    print(f'Olá, {nome}')

# O parâmetro atua como uma variável que armazena um valor. Ainda não tem um valor interno
# Para passar um valor para a variável, colocamos entre parênteses quando chamamos a função
ola_nome('Maycon')


