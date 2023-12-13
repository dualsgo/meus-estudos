# Exercício Python #063 - Sequência de Fibonacci v1.0 - Aula 00 até 14 - Mundo 2
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# Solicita ao usuário a entrada de um número que representa a quantidade de termos na sequência.
termos = int(input('Digite quantos termos deseja visualizar: '))

# Inicializa os primeiros dois termos da sequência de Fibonacci.
primeiro_termo = 0
segundo_termo = 1

# Inicializa a variável que armazenará o próximo termo na sequência.
proximo_termo = 0

# Imprime os dois primeiros termos da sequência de Fibonacci.
print(f'{proximo_termo} - {segundo_termo} - ', end='')
termos = termos - 2

# Enquanto ainda houver termos para serem gerados na sequência.
while termos > 0:

    # Calcula o próximo termo somando os dois termos anteriores.
    proximo_termo = primeiro_termo + segundo_termo

    # Imprime o próximo termo calculado na sequência, seguido por um traço e um espaço.
    print(proximo_termo, end='')
    print(' - ' if termos != 1 else '.', end='')

    # Atualiza os termos anteriores para os próximos cálculos.
    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo

    # Decrementa o número de termos restantes na sequência.
    termos -= 1
