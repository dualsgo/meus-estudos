# MIMO - 6 - Operações com listas
# 06.5 - Contando elementos

# Ao explorar conjuntos de dados, é bom saber quantas vezes um dado está presente, como a resposta mais frequente a uam pesquisa.
respostas = ['sim', 'não', 'as vezes', 'sim', 'sim']

# Para contar a frequência que um valor aparece em uma lista como, começamos com o nome da lista, um ponto e em seguida o método count(), com o valor desejado entre os parênteses
# Podemos salvar o resultado da consulta em uma variável para reutilizá-la depois.
frequencia = respostas.count('sim')
print(frequencia)

# Podemos usar qualquer tipo de valor.

# Se não quisermos saber o número exato, mas apenas se existe um elemento específico, usamos a palavra-chave in
# O resultado será um boolean, True se houver o item na lista, caso contrário, False
print('não' in respostas)

