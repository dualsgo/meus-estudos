# Exercício Python #015 - Aluguel de Carros - Aula 00 até 07 - Mundo 1
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
from emoji import emojize

# Tarefa 1: Perguntar a quantidade de Km percorridos e a quantidade de dias alugados.
print(emojize(':carro: ALUGUEL DE CARROS :carro:', language='pt'))
dias_alugados = int(input(emojize(':relógio_temporizador: Digite a quantidade de dias que utilizou o veículo: ', language='pt')))

km_percorrido = float(input(emojize(':carro_se_aproximando: Digite a quantidade de Km percorridos: Km ', language='pt')))

# Tarefa 2: Calcular os valores a pagar.
valor_diaria = 60
total_diaria = dias_alugados * valor_diaria
print(f'Você alugou o veículo por {dias_alugados} dias. O valor total devido é de R$ {total_diaria:.2f}.')

valor_km = 0.15
total_por_km = km_percorrido * valor_km
print(f'Você rodou {km_percorrido} Km. O valor total devido é de R$ {total_por_km:.2f}.')

# Tarefa 3: Exibir os resultados
total = total_diaria + total_por_km
print(f'O valor da sua conta é de R$ {total:.2f}.')