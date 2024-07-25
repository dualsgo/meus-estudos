# Exercício Python #048 - Soma ímpares múltiplos de três - Aula 00 até 13 - Mundo 2
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# Tarefa 1: Iniciar o acumulador para verificar a soma e um contador para saber quantos são.
contador = 0
acumulador = 0
# Tarefa 2: Verificar todos os números entre 1 e 500 para saber se são múltiplos de 3.
for numero in range(1, 500):
    impar = numero % 2 != 0
    multiplo_tres = numero % 3 == 0
    if multiplo_tres and impar:
        acumulador += numero
        contador += 1
        print(f'\033[1;32m{numero}\033[m', end=', ')
    else:
        print(f'\033[1;31m{numero}\033[m', end=', ')
print('FIM!')
print(f'Entre 1 e 500, encontramos {contador} múltiplos de 3 que são ímpares!')
print(f'A soma entre todos estes valores é {acumulador}.')

# Também poderíamos iterar a cada 3 a partir do 3 no range()