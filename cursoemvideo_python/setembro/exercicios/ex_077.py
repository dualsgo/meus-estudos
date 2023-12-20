"""Desafio 077 - Contando vogais em Tupla (Aula 01 a 16): Crie uma tupla com várias palavras (não usar acentos) e depois disso você deve mostrar para cada palavra quais são as suas vogais.
"""
# Criando a tupla com as palavras
palavras = ("python", "programação", "linguagem", "inteligência", "artificial", "algoritmo", "computador", "dados", "análise", "estrutura", "desenvolvimento", "tecnologia")

for palavra in palavras:
    print(f'As vogais da palavra \033[1;32{palavra.upper()}\033[m são: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáâãeéêiíîoõóôouúû':
            print(letra, end=" ")
    print('')