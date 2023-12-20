# Exercício Python #010 - Conversor de Moedas - Aula 00 até 07 - Mundo 1
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.

# Tarefa 1: Ler o valor que a pessoa possui.
carteira = float(input('Digite quanto possui na carteira: R$ '))

# Tarefa 2: Converter os valores
cotacao_dolar = 4.90
cotacao_euro = 5.36
cotacao_peso = 72.89

dolar = carteira / cotacao_dolar
euro = carteira / cotacao_euro
peso = carteira * cotacao_peso

# Tarefa 2: Mostrar quantos dólares ela pode comprar.
print(f'Você possui R$ {carteira:.2f}. Na cotação atual (US$ 1,00 = R$ 3.27) você pode comprar US$ {dolar:.2f}.')
print('')
print(f'Você possui R$ {carteira:.2f}. Na cotação atual (1,00 € = R$ 5.36) você pode comprar {euro:.2f} €.')
print('')
print(f'R$ {carteira:.2f} equivalem a $ {peso:.2f} pesos argentinos.')
