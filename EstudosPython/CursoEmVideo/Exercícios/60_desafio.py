# Exercício Python #060 - Cálculo do Fatorial - Aula 00 até 14 - Mundo 2
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número: '))  # Solicita e converte um número para inteiro
print(f'{numero}! = ', end='')  # Exibe o início da expressão do fatorial
acumulador = numero  # Inicializa o acumulador com o número fornecido

while numero >= 2:
    print(f'{numero} x ', end='')  # Exibe cada multiplicador até 2
    numero -= 1  # Decrementa o número a ser multiplicado
    acumulador *= numero  # Atualiza o acumulador multiplicando pelo próximo número

    if numero == 1:
        print(f'{numero} = ', end='')  # Exibe o último fator e o sinal de igual

print(acumulador)  # Exibe o resultado final do fatorial
