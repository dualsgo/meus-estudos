# MIMO - 08 - Funções
# 08.4 - Usando vários parâmetros

# As funções precisam de vários parâmetros para executar tarefas em mais dados. Podemos criar funções com um único parâmetro ou adicionar mais, os separando com vírgula.
def infos(nome, idade, sexo):
    texto = f'Olá, {nome}. Sua idade é {idade} e o seu sexo é {sexo}.'
    return texto

# Para passar os valores para a função também os separamos com vírgula. Passamos os valores para uma função na ordem dos parâmetros. Podemos adicionar quantos valores quisermos, desde que os separemos por vírgula.
dados = infos('Maycon', 30, 'masculino')

print(dados)