# MIMO - 03 - Declarações Condicionais

# 03.2 - Usando condições

# Podemos usar operadores de comparação em programas para verificar se uma pergunta está correta, por exemplo.
resposta = 'Picasso'
if resposta == 'Picasso':
    print('Certa resposta!')

# Podemos usar um operador de desigualdade para verificar se a resposta não está correta.
if resposta != 'Picasso':
    print('Resposta errada!')

# As instruções if funcionam com todos os operadores de comparação.

# Podemos armazenar o resultado de uma comparação em uma variável e usá-la como condição.
pontos = 51
passou = pontos > 50
if passou:
    print('Pontos suficientes para passar!')