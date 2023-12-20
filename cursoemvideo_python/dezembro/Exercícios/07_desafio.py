# Exercício Python #007 - Média Aritmética - Aula 00 até 07 - Mundo 1
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Tarefa 1: Ler as duas notas
nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
soma_notas = nota_1 + nota_2
# tarefa 2: Calcula-las e mostrar a média.
media = soma_notas / 2

print(f'Sua primeira nota foi {nota_1} e a segunda nota foi {nota_2}.')
print(f'A sua média ficou {media:.1f}!')
# .1f arredonda segundo as regras algébricas
