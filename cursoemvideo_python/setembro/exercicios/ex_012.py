"""Desafio 012 - Calculando Descontos (Aula 01 a 07): Faça um algoritimo que leia o preço de um produto e seu novo preço com 5% de desconto."""

# Passo 1: Ler o preço do produto - Armazenamos o preço em uma variável convertida para float
print('Calculadora de descontos!\nDigite o preço em R$:')
preco = float(input(''))
print(f'O valor digitado foi: \033[1;32mR$ {preco:.2f}\033[m')
# Calcular e exibir o desconto - Calculamos o desconto pegando o preço e subtraindo dele o valor total multiplicado pelo valor da porcentagem, respeitando a ordem de precedência.
valor_final = preco - (preco * 5/100)  # Exibe o valor com desconto
valor_desconto = preco - valor_final  # Exibe o valor do desconto

print(f"""
O valor do produto sem desconto é \033[1;32mR$ {preco:.2f}\033[m.
Com 5% de desconto (\033[1;32mR$ {valor_desconto:.2f}\033[m) o valor final será de \033[1;32mR$ {valor_final:.2f}\033[m.""")
