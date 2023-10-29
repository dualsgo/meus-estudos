"""Desafio 033 - Jogo de Adivinhação V.1.0 (Aula 01 a 10): Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

print("""
      \033[1;45mMENOR E MAIOR\033[m""")
# Passo 1: Atribuir a uma variável uma lista, cada elemento será definido por uma escolha do usuário - Usaremos input para atribuir o valor de cada elemento da lista
numeros = [input('Digite o primeiro número: '), input(
    'Digite outro número: '), input('Digite o último número: ')]
# Passo 2: Exibe a lista dos números digitados e mostra o menor e maior valor.
print(
    f"\n\033[7mVocê digitou os seguintes números:\033[m \033[1m{', '.join(numeros)}\033[m.")
# Agora exibe o maior e o menor da lista:
print(f"""
\033[7mO menor número da lista é:\033[m \033[1m{min(numeros)}\033[m.
\033[7mO maior número da lista é:\033[m \033[1m{max(numeros)}\033[m.
""")
