# MIMO - 05 - Listas
# 05.2 - Alterando dados em listas

# Vamos nos aprofundar no gerenciamento de listas e em como atualizar os dados contidos nelas. Por exemplo, como os dados de temperatura podem mudar ao longo do dia.
temperature = [17, 20, 26, 24]
print(temperature)

# As listas podem armazenar qualquer dado, seja string, boolean, ponto flutuante ou inteiro.
# Cada elemento de uma lista possui uma posição chamada índice.
# Os índices começam em zero e aumentam com cada valor adicional. Isso significa que o segundo elemento está no índice [1].
print(temperature[1])

# Para alterar o terceiro valor de temperature na lista, acessamos o valor através do seu índice e usamos = para atribuir a ele um novo valor
temperature[2] = 25
print(temperature)
