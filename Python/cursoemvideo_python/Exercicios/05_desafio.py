# Exercício Python #005 - Antecessor e Sucessor - Aula 00 até 07 - Mundo 1
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# Tarefa 1: Ler um número
numero = int(input('Digite um número: '))

# Tarefa 2: Mostrar seu antecessor e sucessor - Se os dados forem utilizados posteriormente, o ideal é salvá-los em uma variável.
antecessor = numero - 1
sucessor = numero + 1

print(f'Você digitou o número {numero}.')
print(f'Analisando o valor {numero}, seu antecessor é {antecessor} e o seu sucessor é {sucessor}.')
