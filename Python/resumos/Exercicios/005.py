# Exercício Python #005 - Antecessor e Sucessor
# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1

print(f'{'RETA NUMÉRICA':^25}')
print(f'{'|':-^5}{'-'*5}{'|':-^5}{'-'*5}{'|':-^5}')
print(f'{antecessor:^5}{numero:^15}{sucessor:^5}')