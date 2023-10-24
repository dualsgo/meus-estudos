"""Desafio 015 - Aluguel de Carros (Aula 01 a 07): Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
"""
# Passo 1: Ler os km e a quantidade de dias - Armazenaremos cada valor em uma variável
print('Digite a quantidade de dias que utilizou o veículo:')
dias = int(input(''))  # Os dias serão convertidos para int
print('Digite a quantidade de Km rodados:')
# Os km serão convertidos para float para permitir valores quebrados
km = float(input(''))

# Passo 2: Definir os valores do Km e do dia
# Primeiro convertemos os km para metros para multiplicar pelo preço e calculamos o custo por Km
custo_km = km * 0.15  # Custo por quilômetro rodado
custo_dia = 60  # Custo por dia de aluguel

# Cálculo dos custos
dias_final = dias * custo_dia  # Custo total dos dias
km_final = custo_km  # Custo total dos Km rodados
aluguel = dias_final + km_final  # Custo total do aluguel

# Exibir os resultados
print(f"""
Você utilizou o veículo por {dias} dias.
A diária custa R$ 60,00 - Você pagará R$ {dias_final:.2f}.
Você rodou por {km} Km.
Cada Km rodado custa R$ 0,15 - Você pagará R$ {km_final:.2f}. 

O custo total do aluguel é R$ {aluguel:.2f}.
""")
