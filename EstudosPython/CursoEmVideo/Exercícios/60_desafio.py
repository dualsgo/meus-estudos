# Exercício Python #060 - Cálculo do Fatorial - Aula 00 até 14 - Mundo 2
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial  # Importa a função factorial do módulo math

# Solicita e converte um número para inteiro, em seguida, imprime o fatorial usando a função factorial
numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é {factorial(numero)}.')

print(f'{numero}! = ', end='')  # Exibe o início da expressão do fatorial
fatorial = 1  # Inicializa o acumulador com o número fornecido

# Utilizando WHILE

while numero > 0:
    print(f'{numero}', end='')  # Exibe cada multiplicador
    print(' x ' if numero > 1 else ' = ', end='')  # Exibe ' x ' para multiplicadores intermédios e '=' para o último
    fatorial *= numero  # Atualiza o acumulador multiplicando pelo próximo número
    numero -= 1  # Decrementa o número a ser multiplicado

print(fatorial)  # Exibe o resultado final do fatorial

# Utilizando FOR

# Solicita e converte um novo número para inteiro
numero = int(input('Digite um número: '))
# Imprime o resultado do fatorial usando a função factorial
print(f'O fatorial de {numero} é {factorial(numero)}.')

for f in range(numero, 0, -1):
    print(f'{f}', end='')  # Exibe cada multiplicador
    print(' x ' if f > 1 else ' = ', end='')  # Exibe ' x ' para multiplicadores intermédios e '=' para o último
    fatorial *= f  # Atualiza o acumulador multiplicando pelo próximo número

print(fatorial)  # Exibe o resultado final do fatorial


