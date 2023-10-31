"""Desafio 038 -  (Aula 01 a 12): Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""
print("""
COMPARANDO NÚMEROS
""")
# Ler dois números inteiros
print('Digite um número:')
esquerda = int(input(''))
print('Digite outro número:')
direita = int(input(''))
# Comparar os números e mostra na tela as mensagens
if esquerda != direita:  # EXTRA - Verifica se os valores são diferentes
    print('Os valores são diferentes!')
    if esquerda > direita:
        print(f'O número {esquerda} é maior que o {direita}.')
    else:
        print(f'O número {direita} é maior que o {esquerda}.')
else:
    print(
        f'Os valores digitados foram: {esquerda} e {direita}.\nEstes valores são iguais!')
