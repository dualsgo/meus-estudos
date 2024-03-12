# Exercício Python #055 - Maior e menor da sequência - Aula 00 até 13 - Mundo 2
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Tarefa 1: Ler cinco pesos
menor_peso = maior_peso = 0  # Inicializa as variáveis para o menor e o maior peso

# Tarefa 2: Mostra o maior e o menor lidos

for i in range(5):  # Loop para iterar cinco vezes
    peso = float(input('Digite seu peso: Kg '))  # Solicita e converte o peso para um número de ponto flutuante

    if i == 0:
        menor_peso = maior_peso = peso  # Se for o primeiro peso, define o menor e o maior como o valor lido

    else:
        # Verifica se o peso atual é maior que o maior peso registrado até agora
        if peso >= maior_peso:
            maior_peso = peso

        # Verifica se o peso atual é menor que o menor peso registrado até agora
        if peso <= menor_peso:
            menor_peso = peso

# Exibe os resultados
print(f'Menor peso: {menor_peso}Kg')
print(f'Maior peso: {maior_peso}Kg')


