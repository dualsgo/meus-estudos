# MIMO - 08 - Funções
# 08.6 - Funções e escopo variável

# Escopo local
# Variáveis criadas dentro de uma função possuem escopo local. Com escopo local, só podemos acessar ou atualizar a variável dentro da função que a criou.

def add_bonus(salario):
    bonus = 100
    bonus = 200 # Podemos atualizar o valor da variável
    print(salario + bonus)

# Se tentarmos acessar a variável fora da função, receberemos um erro.
# print(bonus) - NameError: name 'bonus' is not defined

# Escopo global
# Variáveis criadas fora de um bloco funcional têm um escopo global. Com um escopo global, podemos acessar a variável em qualquer lugar do código.

# Todas as variáveis têm escopo global, exceto aquelas criadas dentro de funções
# Há uma exceção para variáveis criadas dentro de funções. Se usarmos a palavra-chave global para declarar uma variável, podemos acessá-la fora da função.

# Mesmo com o escopo global, é importante que só possamos acessar as variáveis após criá-las.

# Se usarmos os mesmos nomes de variáveis dentro e fora de uma função, o Python usará a variável local dentro da função.
# Exemplo:
bonus = 100 # Variável global

def add_bonus(salario):
    bonus = 200  # Variável 
    print(salario + bonus)

print(bonus) # 100 - A variável global bonus será usada valor 100
print(add_bonus(1000)) # 1200 - A função usará a variável local bonus que criamos dentro dela valor 200