# Exercício Python #027 - Primeiro e último nome de uma pessoa
# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza)

nome = input('Digite o seu nome: ').strip().title().split()

print(f'{' '.join(nome):<{len(nome)}}')
print(f'{nome[0]:.<{len(' '.join(nome))}}')
print(f'{nome[-1]:.>{len(' '.join(nome))}}')