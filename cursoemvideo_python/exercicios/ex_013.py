"""Desafio 013 - Reajuste Salarial (Aula 01 a 07): Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento."""

# Ler o salário de um funcionário - Armazenamos o valor digitado pelo usuário em um avariável utilizando a função input
print('Digite o valor atual do seu salário: ')
salario_atual = float(input(''))
print(f'O seu salário atual é \033[1;32mR$ {salario_atual:.2f}\033[m')

# Mostrar o novo salário com 15% de aumento - O novo salário ficará armazenado em uma variavel. Ele corresponde a soma do salario atual mais o produto do salario atual vezes 1,5
novo_salario = salario_atual + (salario_atual * 15/100)
aumento = novo_salario - salario_atual
print(f'O seu novo salário é de \033[1;32mR$ {novo_salario:.2f}\033[m.')
print(f'O aumento de 15% equivale a \033[1;32mR$ {aumento:.2f}\033[m.')
