"""Desafio 021 - Título (Aula 01 a 09): Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

EX.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nome = str(input('')).strip()

nome_separado = nome.split()
print(nome_separado)
primeiro_nome = nome_separado[0]
print(primeiro_nome)
ultimo_nome = nome_separado[-1]
print(ultimo_nome)
