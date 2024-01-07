# MIMO - 03 - Declarações Condicionais

# 03.5 - Usando decisões complexas

# Operador and (e)

# Vejamos como os programas atuam em decisões complexas. Sabemos como executar ou pular código como base em uma condição. Mas e se quiséssemos verificar duas ou mais condições?

# O operador and nos permite executar código somente se ambas as condições forem True. Ele ignora o bloco de código se uma ou mais condições forem False.
# Nesse exemplo só poderá dirigir se tiver 18 ou mais e possuir habilitação
idade = 30
carteira_habilitacao = True

# Nesse exemplo só poderá dirigir se tiver 18 ou mais e possuir habilitação
if idade >= 18 and carteira_habilitacao == True:
    # Se a idade for maior ou igual a 18 e possuir habilitação, o bloco if será executado.
    print('Pode dirigir.')
else:
    # Se a idade for menor que 18 ou não possuir habilitação, o bloco else será executado.
    print('Não pode dirigir!')

# Podemos adicionar quantas condições quisermos

# Operador or (ou)

# Para executar o código quando uma das condições for True, usamos o operador or (ou). Com ele, o código só será ignorado se todas as condições forem False.

# Nesse exemplo o aluno só será liberado se o pai ou a mãe estiverem presentes
pai = False
mae = False

if pai or mae:
    # Se o pai ou a mãe estiverem presentes, o bloco if será executado.
    print('Aluno liberado')
else:
    # Se o pai e a mãe não estiverem presentes, o bloco else será executado.
    print('Aluno não liberado!')

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

# Podemos usar instruções if, elif e else dentro de outras. A indentação precisa ser colocada corretamente para separar as instruções
idade = 14

# Primeira condição - Verifica se tem pelo menos 16 anos. Se sim, o bloco if será executado.
pode_votar = idade >= 16

# Segunda condição - Verifica se a idade está entre 18 e 70, para saber se o voto é obrigatório.
obrigatorio = 18 <= idade <= 70

if pode_votar:
    # Se a idade for maior ou igual a 16, o bloco if será executado.
    print('Pode votar!')
    if obrigatorio:
        # Se a idade for maior ou igual a 18 e menor ou igual a 70, o bloco if será executado.
        print('Voto obrigatório!')
    else:
        # Se a idade for menor que 18 ou maior que 70, o bloco else será executado.
        print('Voto facultativo!')
else:
    # Se a idade for menor que 16, o bloco else será executado.
    print('Não pode votar!')
