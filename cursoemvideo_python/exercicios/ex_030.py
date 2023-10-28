"""Desafio 030 - Par ou ímpar? (Aula 01 a 10): Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. """
print("""
      PAR OU ÍMPAR?""")
# Passo 1: Ler o número - Utilizamos input para receber o valor e atribuímos o método a uma variável
print('\033[1mDigite um número para saber...\033[m\n')
numero = int(input(''))
# Verificar se é par ou ímpar - Comparamos se o valor digitado ao ser dividido por 2 terá resto 0 ou 1. Se for zero atenderá a condição, retornará True e será exibida a mensagem informando que o número digitado é par, caso contrário ele será considerado ímpar
if numero % 2 == 0:
    print(f'\033[1;42mO número {numero} é par!\033[m')
else:
    print(f'\033[1;41mO número {numero} é ímpar!\033[m')
