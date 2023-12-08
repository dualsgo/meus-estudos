# Exercício Python #032 - Ano Bissexto - Aula 00 até 09 - Mundo 1
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from random import randint
from datetime import date

# Tarefa 1: Ler um ano
ano = randint(1582, 2024)
if ano == 0:
    ano = date.today().year
# Tarefa 2: Verificar se é bissexto
# É um número divisível por 4, mas não é divisível por 100.
caso_1 = ano % 4 == 0 and ano % 100 != 0
# É um número divisível por 4, por 100 e por 400.
caso_2 = ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0

if caso_1 or caso_2:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
