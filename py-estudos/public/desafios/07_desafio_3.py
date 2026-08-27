# MIMO - 07 - Operações com strings - Desafio 1
# Uma locadora de DVD deseja atualizar seu site com um cabeçalho que liste os filmes mais vendidos.
top_filmes = "The Power of the Dog - Trapped - Tenet"
print(top_filmes)

# Tarefa 1: Crie uma nova variável novos_top_filmes que substitua o valor "Trapped" de top_filmes por "Moonfall" . Lembre-se de que esses títulos diferenciam maiúsculas de minúsculas.
novos_top_filmes = top_filmes.replace('Trapped', 'Moonfall')

# Tarefa 2: Imprima a nova lista
print(novos_top_filmes)