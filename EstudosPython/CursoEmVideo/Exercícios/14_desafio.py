# Exercício Python #014 - Conversor de Temperaturas - Aula 00 até 07 - Mundo 1
# Escreva um programa que converta uma temperatura digitada em °C para °F

# Fórmula °F = °C x 9  5 + 32
# Fórmula °C = 5 ÷ 9 (°C - 32)
# Tarefa 1: Receber a temperatura em °C
temperatura_em_celsius = float(input('Digite a temperatura em °C: '))

# Tarefa 2: Converter e exibir em °F
temperatura_em_fahrenheit = temperatura_em_celsius * (9 / 5) + 32
print(f'A temperatura {temperatura_em_celsius} °C equivale a {temperatura_em_fahrenheit} °F.')
