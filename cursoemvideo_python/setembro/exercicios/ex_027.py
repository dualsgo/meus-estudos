"""Desafio 027 - Primeiro e último nome de uma pessoa (Aula 01 a 09): Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

EX.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
# Passo 1: Ler o nome completo - Armazenamos o nome utilizando a função input atribída a uma variável. A string recebe um pré tratamento para remover espaços desnecessários.
print('\033[1;45mNOME E SOBRENOME\033[m')
nome = str(input('')).strip()
# Passo 2: Criar variáveis para os nomes - Uma variável recebe o nome digitado separado em lista com o método split
nome_separado = nome.split()
# Depois basta exibir primeiro índice e o último
primeiro_nome = nome_separado[0]
print(
    f'\033[1;31mO primeiro nome digitado foi: \033[m\033[1m{primeiro_nome.upper()}\033[m.')
ultimo_nome = nome_separado[-1]
print(
    f'\033[1;31mO último nome digitado foi: \033[m\033[1m{ultimo_nome.upper()}\033[m.')
