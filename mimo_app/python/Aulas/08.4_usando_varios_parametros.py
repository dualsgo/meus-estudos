# MIMO - 08 - Funções
# 08.4 - Usando vários parâmetros

# As funções precisam de vários parâmetros para executar tarefas em mais dados. Podemos criar funções com um único parâmetro ou adicionar mais, os separando com vírgula.
def infos(nome, idade, sexo):
    texto = f'Olá, {nome}. Sua idade é {idade} e o seu sexo é {sexo}.'
    return texto

# Para passar os valores para a função também os separamos com vírgula. Passamos os valores para uma função na ordem dos parâmetros. Podemos adicionar quantos valores quisermos, desde que os separemos por vírgula.
dados = infos('Maycon', 30, 'masculino')

print(dados)

# Se não passarmos os valores na ordem dos parâmetros, eles serão atribuídos aos parâmetros na ordem em que os passamos. Para contornar isso, podemos passar os valores com o nome dos parâmetros.
dados = infos(idade=30, nome='Maycon', sexo='masculino')

# Outra precaução que podemos tomar é definir um valor padrão para um parâmetro. Isso significa que, se não passarmos um valor para o parâmetro, ele usará o valor padrão.
def infos(nome, idade, sexo='não informado'):
    texto = f'Olá, {nome}. Sua idade é {idade} e o seu sexo é {sexo}.'
    return texto

# Agora podemos chamar a função sem passar um valor para o parâmetro sexo.
dados = infos('Maycon', 30)

print(dados)
