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
    
    
# Versão 2 - Completa


def recebe_ano(mensagem):
    """
    Pede ao usuário para digitar um ano e garante que o valor digitado seja um número inteiro.
    """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Valor de tipo inválido! Por favor, digite um número inteiro.')


def verifica_ano(year):
    """
    Verifica se o ano fornecido é bissexto.
    Um ano é bissexto se for divisível por 4 e (não divisível por 100 ou divisível por 400).
    """
    if year > 1582:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    else:
        return False


# Pede ao usuário para digitar um ano
ano = recebe_ano('Digite o ano que deseja verificar: ')

# Verifica se o ano é bissexto
bissexto = verifica_ano(ano)

# Exibe o resultado formatado
if bissexto:
    print(f'O ano {ano} \033[1;32mé bissexto!\033[m')
else:
    print(f'O ano {ano} \033[1;31mnão é bissexto!\033[m')


ano_atual = date.today().year

# Laço para exibir a lista de anos
#for i in range(1582, ano_atual + 1):
#	print(f'O ano {i}', '\033[1;32mé bissexto!\033[m' if verifica_ano(i) else '\033[1;31mnão é bissexto!\033[m')
