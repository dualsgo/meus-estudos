"""Desafio 020 - Sorteando uma ordem na lista (Aula 01 a 08): O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia os nomes dos quatro alunos e mostre a ordem sorteada.
"""
# Passo 1: Importar a biblioteca random
from random import shuffle, sample
# Passo 2: Entrar com os nomes - Para isso vamos armazenar cada nome em uma variável usando input para solicitar os valores
primeiro_nome = input('Digite o nome do primeiro aluno: ')
segundo_nome = input('Agora é a vez do segundo: ')
terceiro_nome = input('Próximo aluno: ')
quarto_nome = input('Por fim, o último aluno: ')

# Passo 3: Criar uma lista com os nomes - Vamos criar a lista atribuindo a uma variável as outras
lista = [primeiro_nome, segundo_nome, terceiro_nome, quarto_nome]

# Passo 4: Exibir a lista embaralhada - Para isso usamos um método shuffle() da biblioteca para embaralhar as strings

shuffle(lista)  # Embaralha a lista
print(f"""A ordem de apresentação será a seguinte: { ", ".join(lista)}""")
# Neste código, ", ".join(lista) combina os elementos da lista com uma vírgula e um espaço entre eles, criando uma única string. Esta string é então exibida como a ordem de apresentação sem colchetes ou aspas simples.

# Se quiser mostrar um número limitado de resultados podemos usar sample(lista, k=quantidade)
print(", ".join(sample(lista, k=2))) # Exibira 2 entre os 4