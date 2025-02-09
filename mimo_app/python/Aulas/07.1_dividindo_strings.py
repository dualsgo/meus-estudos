# MIMO - 07 - Operações com strings
# 07.1 - Dividindo strings

# Ao trabalhar com diferentes tipos de dados, muitas vezes os receberemos em um formato que pode dificultar o trabalho.
# Conseguimos dividir strings e armazenar os valores individuais numa lista utilizando o método .split()
# Uma string é uma sequência de caracteres. Podemos pensar em uma string como uma lista de caracteres.
nome_completo = "Maycon Douglas Barros da Silva" 
print(nome_completo)

# As strings são separadas em espaços em branco por padrão. Podemos ver isso se exibirmos a string como uma lista.
lista = nome_completo.split()
print(lista) # ['Maycon', 'Douglas', 'Barros', 'da', 'Silva']
# Cada item da lista recebe um índice, começando em 0. Podemos acessar qualquer item da lista usando seu índice.
print(lista[0]) # Maycon

# Além disso, cada caractere em uma string também recebe um índice. Podemos acessar qualquer caractere em uma string usando seu índice. O primeiro índice representa o item da lista que queremos acessar e o segundo índice representa o caractere dentro do item.
print(lista[0][0]) # M

# Podemos usar o método .split() para dividir uma string em qualquer caractere que quisermos.
# Podemos especificar exatamente como queremos dividir uma string colocando um separador entre parênteses.
# Por exemplo, se quisermos dividir uma string em cada vírgula, colocamos a vírgula entre parênteses.

