# Exercício Python #012 - Calculando Descontos - Aula 00 até 07 - Mundo 1
# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# Tarefa 1: Ler o preço de um produto
preco = float(input('Digite o valor do produto: R$ '))

# Tarefa 2: Mostrar o novo preço com 5% de desconto.
desconto = preco * (5/100)
print(f'Você recebeu 5% de desconto! (R$ {desconto:.2f})')

novo_preco = preco - desconto

# Tarefa 3: Mostrar o resultado
print(f'Sua compra de R$ {preco:.2f}, com desconto será R$ {novo_preco:.2f}.')
