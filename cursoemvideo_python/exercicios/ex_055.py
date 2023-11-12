"""Desafio 055 - Maior e menor da sequência (Aula 01 a 13): Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior peso e o menor peso."""

# Definir uma variável que receberá uma lista
peso = []
# Define o intervalo desejado, no caso 6
for i in range(6):
# Adiciona os valores a lista através de um input() combinado com o método append()
    peso.append(float(input('Digite um peso: Kg ')))
    print(f'Você digitou {peso[-1]} Kg') # Acessamos o último elemento para exibi-lo após digitado
# Os métodos sum, min e max facilitam mostrar o resultado
print(f'\033[1mTodos juntos pesam:\033[m \033[1;31m{sum(peso)}Kg\033[m\n\033[1;32mO mais leve pesa: {min(peso)}Kg\033[m\n\033[1;31mO mais pesado pesa: {max(peso)}Kg\033[m.')