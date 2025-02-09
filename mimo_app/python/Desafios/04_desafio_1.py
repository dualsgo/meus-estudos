# MIMO - 04 - Loops - Desafio 1
# Crie um programa de inventário simples para uma loja de camisas. O programa deve aumentar a variável sales em 1 e diminuir a variável inventory em 1 quando uma camisa for vendida.

# Tarefa 1: Entre a inicialização da variável e as instruções de impressão, aumente o valor da variável sales em 1 usando um operador
vendas = 0
print(f'Vendas: {vendas}')
estoque = 10
print(f'Estoque: {estoque}')

print('Venda realizada!')
vendas += 1

# Tarefa 2: Diminua o valor da variável inventory em 1 usando um operador.
estoque -= 1
print(f'Vendas: {vendas}')
print(f'Estoque: {estoque}')
