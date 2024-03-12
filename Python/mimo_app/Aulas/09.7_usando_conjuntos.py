# MIMO - 09 - Tuplas, dicionários e conjuntos
# 09.7 - Usando conjuntos

# Para adicionar um novo valor a um conjunto como answers, codificamos o nome do conjunto, seguido da instrução .add() como o novo valor entre os parênteses.
conjunto = {'sim', 'não'}
print(conjunto)

conjunto.add('talvez')
# Os itens não são ordenados, portanto, não podemos ter certeza da ordem em que os itens aparecerão quando impressos
print(conjunto)

# Como os conjuntos excluem os valores duplicados, nada acontece quando tentamos adicionar um valor já existente.
conjunto.add('sim')

# Sabemos que podemos acessar e atualizar elementos em listas pelo seu índice, mas ao contrário das listas, os conjuntos não podem ser ordenados. Isso significa que os elementos não possuem índices e devido isso, só podemos verificar se um elemento está presente no conjunto usando o operador in

print('sim' in conjunto)

# Também podemos usar um loop for para iterar pelos elementos do conjunto e acessá-los um por um

for elemento in conjunto:
    print(f'Opção: {elemento}')

# Para remover um elemento do conjunto como 'sim', codificamos o nome do conjunto seguido da instrução .remove() com o elemento entre parênteses. Para evitar erros verificamos antes se o elemento pertence ao conjunto.

if 'sim' in conjunto:
    conjunto.remove('sim')
print(conjunto)