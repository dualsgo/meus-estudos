"""Desafio 038 - Comparando números (Aula 01 a 12): Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""
# Cores
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}
print(f"""
{cor['destaque']}COMPARANDO NÚMEROS{cor['fecha']}
""")
# Ler dois números inteiros
print('Digite um número:')
esquerda = int(input(''))
print('Digite outro número:')
direita = int(input(''))
# Comparar os números e mostra na tela as mensagens
if esquerda != direita:  # EXTRA - Verifica se os valores são diferentes - Se forem, precisamos de um retorno caso o número da esquerda seja maior e outra caso o da direita seja maior
    print(f'{cor["red"]}Os valores são diferentes!{cor["fecha"]}')
    if esquerda > direita:
        print(f'O número {cor["green"]}{esquerda}{cor["fecha"]} é maior que o {cor["red"]}{direita}{cor["fecha"]}.')
    else:
        print(f'O número {cor["green"]}{direita}{cor["fecha"]} é maior que o {cor["red"]}{esquerda}{cor["fecha"]}.')
else: # Se forem iguais só precisamos de uma opção
    print(
        f'Os valores digitados foram: {cor["green"]}{esquerda}{cor["fecha"]} e {cor["red"]}{direita}{cor["fecha"]}.\n{cor["green"]}Estes valores são iguais!{cor["fecha"]}')
