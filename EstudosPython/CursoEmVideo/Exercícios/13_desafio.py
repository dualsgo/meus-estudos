# Exercício Python #013 - Reajuste Salarial - Aula 00 até 07 - Mundo 1
# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Tarefa 1: Ler o salário de um funcionário
salario_atual = float(input('Digite o seu salário atual: R$ '))

# Tarefa 2: Calcular o aumento (15%)
aumento = salario_atual * (15/100)
novo_salario = salario_atual + aumento

# Tarefa 3: Exibir o novo salário
print(f'Seu novo salário, com 15% de aumento será R$ {novo_salario:.2f}.')
print(f'O aumento equivale a R$ {aumento:.2f}.')