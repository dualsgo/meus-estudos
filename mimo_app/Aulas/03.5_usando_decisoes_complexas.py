# MIMO - 03 - Declarações Condicionais

# 03.5 - Usando decisões complexas

# Operador and (e)

# Vejamos como os programas atuam em decisões complexas. Sabemos como executar ou pular código como base em uma condição. Mas e se quiséssemos verificar duas ou mais condições?

# O operador and nos permite executar código somente se ambas as condições forem True. Ele ignora o bloco de código se uma ou mais condições forem False.

idade = 30
carteira = False
# Nesse exemplo só poderá dirigir se tiver 18 ou mais e possuir habilitação
if idade >= 18 and carteira == True:
    print('Pode dirigir.')
else:
    print('Não pode dirigir!')

# Podemos adicionar quantas condições quisermos

# Operador or (ou)

# Para executar o código quando uma das condições for True, usamos o operador or (ou). Com ele, o código só será ignorado se todas as condições forem False.

idade = 45

# Primeira condição - Verifica se tem pelo menos 16 anos. Se sim, o bloco if será executado.
pode_votar = idade > 15

# Segunda condição - Verifica se a idade está entre 18 e 70, para saber se o voto é obrigatório.
obrigatorio = 18 <= idade <= 70

if pode_votar:
    print('Pode votar!')
    if obrigatorio:
        print('Voto obrigatório!')
    else:
        print('Voto facultativo!')
else:
    print('Não pode votar!')

# OPERADOR AND (e) - Ambos precisam ser True
# TRUE + TRUE = TRUE
# TRUE + FALSE = FALSE
# FALSE + TRUE = FALSE
# FALSE + FALSE = FALSE

# OPERADOR OR (ou) - Pelo menos um precisa ser True
# TRUE + TRUE = TRUE
# TRUE + FALSE = TRUE
# FALSE + TRUE = TRUE
# FALSE + FALSE = FALSE
