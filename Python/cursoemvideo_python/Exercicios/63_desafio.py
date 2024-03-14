# Exercício Python #063 - Sequência de Fibonacci v1.0 - Aula 00 até 14 - Mundo 2
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# Solicita ao usuário a entrada de um número que representa a quantidade de termos na sequência.
termos = int(input('Digite quantos termos deseja visualizar: '))

# Inicializa os termos da sequência de Fibonacci.
primeiro_termo = 0
segundo_termo = 1

# Imprime os termos da sequência de Fibonacci usando um loop while.
contador = 0
while contador < termos:
    print(primeiro_termo, end=' ')
    primeiro_termo, segundo_termo = segundo_termo, primeiro_termo + segundo_termo
    contador += 1


