"""Desafio 005 - Antecessor e sucessor (Aula 01 a 07): Faça um programa que leia um número inteiro e mostre na tela o seu sucesso e seu antecessor."""

# Passo 1: Receber do usuário o número que deseja saber as informações. Para isso vamos guardar este valor em uma variável.
print('\033[1;31mAntecessor\033[m e \033[1;32msucessor\033[m\nDigite um número!')
numero = int(input(''))
# A variável utiliza o método input() para receber o valor e o método int() converte o valor para um número inteiro.

# Passo 2: Exibir o resultado: Para isso iremos subtrair 1 do valor para mostar o antecessor e somar 1 para mostar o sucessor. Para melhor entendimento iremos criar uma variavel para cada um dos casos mas seria possível utilizar a expressão diretamente no print

antecessor = numero - 1
sucessor = numero + 1

print(
    f'Você digitou o número \033[1m{numero}\033[m!\n\033[31mO seu antecessor é o número {antecessor}.\033[m\n\033[32mO seu sucessor é o número {sucessor}.\033[m')

print(
    f'RETA NUMÉRICA: - < --- ... ,{antecessor}, {numero}, {sucessor}, ... ---> +')
