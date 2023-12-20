"""Desafio 075 - Análise de dados em uma Tupla (Aula 01 a 16): Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

- Quantas vezes apareceu o valor 9
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares
"""

# Criar a tupla que irá armazenar quatro valores
tupla = int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: '))

print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 not in tupla:
    print('O número 3 não aparece na lista!')
else:
    print(f'O número 3 apareceu na posição {tupla.index(3) + 1}.')
print('Os seguintes itens da tupla são pares: ', end='')
for item in tupla:
    if item % 2 == 0:
        print(item)

