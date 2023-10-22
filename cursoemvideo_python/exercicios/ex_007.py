"""Desafio 007 - Média Aritimética (Aula 01 a 07): Desenvolva um programa que leia as notas de um aluno, calcule e mostre a média."""

# Passo 1: Ler as notas - Para isso utilizaremos dias variáveis, uma para cada nota.
print('\033[7mMÉDIA ARITIMÉTICA\033[m')
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
# Passo 2: Calcular e exibir a média - Criaremos uma cariável para realizar o cálculo e armazenar o resultado.

# Lembrando da ordem de precedência, nesse caso primeiro realizamos a soma dos valores para depois dividir por 2. Para isso utilizamos os parenteses para envolver a soma.
media = (primeira_nota + segunda_nota) / 2

# Agora exibimos o resultado:

print(f"""Suas notas são \033[1m{primeira_nota}\033[m e \033[1m{segunda_nota}\033[m.
A sua média é \033[1;31m{media}\033[m.""")
