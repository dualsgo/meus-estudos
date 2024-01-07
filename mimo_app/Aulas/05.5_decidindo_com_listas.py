# MIMO - 05 - Listas
# 05.5 - Decidindo com listas

# Vamos descobrir como podemos contar os elementos nas listas e usá-los com instruções if

# Usamos a instrução len() com o nome da lista entre parênteses para obter o número de elementos em uma lista.
# Podemos usar print() para exibir o comprimento de uma lista no console
# Podemos armazenar o comprimento de uma lista em uma variável
users = ['Sarah', 'Mike', 'Ella']
#       [      0,      1,      2]

print(users)
number_of_users = len(users) # Retorna 3
print(number_of_users)

# Podemos usar o comprimento da lista par criar instruções condicionais com base no número de elementos.

if number_of_users < 4:
    # Se o número de usuários for menor que 4, exibimos uma mensagem de erro
    print('Precisamos de mais membros!')
else:
    # Se o número de usuários for maior ou igual a 4, exibimos uma mensagem de sucesso
    print('Temos gente o suficiente!')

# Podemos usar o operador in para verificar se um elemento existe em uma lista e tomar uma decisão com base nisso.
# O operador in retorna True se o elemento existir na lista e False se não existir.

if 'Sarah' in users:
    print('Sarah está na lista')
else:
    print('Sarah não está na lista')
    

# Podemos combinar isso com uma iteração:
sequencia_fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Se quisermos verificar por exemplo os números pares, podemos usar o operador % (módulo)
# O operador % retorna o resto da divisão entre dois números. Se o resto for 0, o número é par, se for 1, o número é ímpar.

# Durante a iteração, podemos criar novas listas e adicionar elementos a elas.
pares = []
impares = []

# Esse loop itera sobre todos os elementos da lista e verifica se o número é par ou ímpar
for numero in sequencia_fibonacci:
    # Se o resto da divisão por 2 for 0, o número é par
    if numero % 2 == 0:
        print(f'O número {numero} é par')
        pares.append(numero)
    else:
        print(f'O número {numero} é ímpar')
        impares.append(numero)
        
print(pares)

# Outras listas podem ser adicionadas a uma lista com o método extend(). A sintaxe é: list.extend(list2)

# Podemos usar o método extend() para adicionar os números pares e ímpares a uma lista de números. extend() adiciona os elementos de uma lista a outra lista. Ele só funciona se os elementos forem do mesmo tipo e se as listas já existirem.
numeros = []
numeros.extend(pares) 
numeros.extend(impares)
print(numeros)

# A função sorted() retorna uma nova lista ordenada com base em uma lista existente. A sintaxe é: sorted(list)
lista_desordenada = [3, 1, 2, 5, 4]
sorted(lista_desordenada) # Retorna [1, 2, 3, 4, 5]
print(f'Lista desordenada após sorted: {lista_desordenada}') # Retorna [3, 1, 2, 5, 4] somente nessa instância
print(lista_desordenada) # Retorna [3, 1, 2, 5, 4]

# A função sorted() não altera a lista existente. Ela retorna uma nova lista ordenada. Podemos atribuir essa nova lista a uma variável.
lista_ordenada = sorted(lista_desordenada)
print(f'Nova lista ordenada após sorted: {lista_ordenada}') # Retorna [1, 2, 3, 4, 5]

# A função sort() ordena a lista existente. A sintaxe é: list.sort()
lista_desordenada = [3, 1, 2, 5, 4]
lista_desordenada.sort() # Retorna [1, 2, 3, 4, 5]
print(f'Lista desordenada após sort: {lista_desordenada}') # Retorna [1, 2, 3, 4, 5]
# A função sort() altera a lista existente. Ela não retorna uma nova lista.

# É importante entender a diferença entre sorted() e sort(). sorted() retorna uma nova lista ordenada e não altera a lista existente. sort() altera a lista existente e não retorna uma nova lista. As listas devem conter apenas elementos do mesmo tipo para serem ordenadas.