# MIMO - 09 - Tuplas, dicionários e conjuntos

# 09.1 - Criando e usando tuplas

# Esta lista contém filmes e datas de lançamento, mas não está claro qual data pertence a qual filme

filmes = ['Vertigo', 'Parasite', 1958, 2010]
# Podemos agrupar dados relacionados com uma tupla.

filmes_tupla = [('Vertigo', 1958), ('Parasite', 2010)]
print(filmes_tupla[1])
# As tuplas nos ajudam a agrupar diferentes partes de dados que pertencem umas às outras.

# Criamos tuplas de forma semelhante a listas, mas utilizamos parênteses em vez de colchetes para envolver os valores. Assim como nas listas, também separamos os elementos com vírgula.

# Como um caso especial, tuplas com apenas um valor terminam em vírgula de qualquer maneira
tulpa_especial = ('Valor',)

# As tuplas podem ter quantos valores quisermos. Podemos salvar uma tupla em uma variável, assim como qualquer valor
