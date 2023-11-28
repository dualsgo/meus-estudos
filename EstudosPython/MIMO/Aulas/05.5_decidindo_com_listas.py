# MIMO - 05 - Listas
# 05.5 - Decidindo com listas

# Vamos descobrir como podemos contar os elementos nas listas e usá-los com instruções if

# Usamos a instrução len() cpm o nome da lista entre parênteses para obter o número de elementos em uma lista.
# Podemos usar print() para exibir o comprimento de uma lista no console
# Podemos armazenar o comprimento de uma lista em uma variável
users = ['Sarah', 'Mike', 'Ella']
print(users)
number_of_users = len(users)
print(number_of_users)

# Podemos usar o comprimento da lista par criar instruções condicionais com vase no número de elementos.
if number_of_users < 4:
    print('Precisamos de mais membros!')
else:
    print('Temos gente o suficiente!')

#

