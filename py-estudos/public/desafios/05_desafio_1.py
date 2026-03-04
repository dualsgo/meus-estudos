# MIMO - 05 - Listas - Desafio 1
# Você decide planejar suas refeições diárias usando Python

# Tarefa 1: Dentro da variável meals, crie uma lista contendo suas refeições de café da manhã, almoço e jantar, nessa ordem: 'omelete', 'salad', e 'chicken'
refeicoes = ['omelete', 'salada', 'frango']
print(f'Menu do café: {refeicoes[0]}')

# Tarefa 2: Altere a primeira declaração impressa para incluir o menu almoço.
print(f'Menu do almoço: {refeicoes[1]}')
print(f'Menu do jantar: {refeicoes[2]}')

# Tarefa 3: Uma migo passa por aqui com pizza! Altere o valor do jantar da lista de meals para pizza.
refeicoes[2] = 'pizza'

# Tarefa 4: Altere a segunda declaração impressa para incluir o item atual do menu do jantar.
print(f'Menu do jantar atualizado: {refeicoes[2]}')