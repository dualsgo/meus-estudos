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

# Versão simplificada
valores = [i for i in range(3, 499, 3) if i % 2 != 0]
print(f'A soma entre os {len(valores)} valores ímpares, múltiplos de 3 no intervalo ente 1 e 500 é {sum(valores)}.')

print(f'Os {len(valores)} valores considerados são:')
for i, v in enumerate(valores):
	print(v, end=', ' if i < len(valores)-1 else '.')

# Recente

soma = quantidade = 0
print('Múltiplos de 3 entre 1 e 500: ', end='')
for i in range(3, 501, 3):
	print(i, end=', ' if i < 498 else '.\n')
	if i % 2:
		soma += i
		quantidade += 1
print(f'A soma entre os {quantidade} números ímpares múltiplos de três entre 1 e 500 é igual a {soma}')