# MIMO - 07 - Operações com strings
# 07.2 - Atualizando strings

# Às vezes precisamos atualizar os dados numa string sem criar uma string totalmente nova.
# Podemos substituir uma parte de uma string armazenada numa variável codificando primeiro o nome da variável e depois o método .replace()
filme = 'Harry Potter e a Pedra Filosofal'
print(f'Filme 1: {filme}')

# Dentro dos parênteses, adicionamos a parte que queremos substituir, uma vírgula e depois o novo valor
novo_filme = filme.replace('Pedra Filosofal', 'Câmara Secreta')
print(f'Filme 2: {novo_filme}')

# Se codificarmos a variável original, notaremos que o valor dela permanece inalterado
print(f'Filme 1: {filme}')

# Quando usamos replace() substituiremos todas as ocorrências do valor dentro da string
