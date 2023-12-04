# MIMO - 08 - Funções
# 08.6 - Funções e escopo variável

# Escopo local
# Variáveis criadas dentro de uam função possuem escopo local. Com escopo local, só podemos acessar ou atualizar a variável dentro da função que a criou.

def add_bonus(salario):
    bonus = 100
    bonus = 200
    print(salario + bonus)

# print(bonus) - NameError: name 'bonus' is not defined
add_bonus(1900)

# Escopo global
# Variáveis criadas fora de um bloco funcional têm um escopo global. Com um escopo global, podemos acessar a variável em qualquer lugar do código.

# Todas as variáveis têm escopo global, exceto aquelas criadas dentro de funções

# Mesmo com o escopo global, é importante que só possamos acessar as variáveis após criá-las.

