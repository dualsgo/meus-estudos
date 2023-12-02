# MIMO - 07 - Operações com strings
# 07.1 - Dividindo strings

# Ao trabalhar com diferentes tipos de dados, muitas vezes os receberemos em um formato que pode dificultar o trabalho.
# Conseguimos dividir strings e armazenar os valores individuais numa lista utilizando o método .split()
nome_completo = "Maycon Douglas Barros da Silva"
print(nome_completo)

# As strings são separadas em espaços em branco por padrão
lista = nome_completo.split()
print(lista)

# Podemos especificar exatamente como queremos dividir uma string colocando um separador entre parênteses.
