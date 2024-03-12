# Exercício Python #050 - Soma dos pares - Aula 00 até 13
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

from random import randint  # Importa a função randint para gerar números inteiros aleatórios
from time import sleep  # Importa a função sleep para pausas temporizadas

# Tarefa 1: Ler 6 números inteiros
soma = 0  # Inicializa a variável para armazenar a soma dos números pares

# Tarefa 2: Mostrar a soma dos que forem pares
for numero in range(6):  # Loop para gerar 6 números
    valor = randint(0, 9999)  # Gera um número inteiro aleatório entre 0 e 9999
    sleep(1)  # Pausa por 1 segundo
    if valor % 2 == 0:  # Verifica se o número é par
        soma += valor  # Adiciona o número à soma
        print(f'\033[1;32mValor {valor} considerado.\033[m')  # Exibe o valor em verde como considerado
    else:
        print(f'\033[1;31mValor {valor} desconsiderado.\033[m')  # Exibe o valor em vermelho como desconsiderado

print(f'A soma dos valores digitados que são pares é {soma}.')  # Exibe a soma final
