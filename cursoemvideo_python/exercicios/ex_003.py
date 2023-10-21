""" Desafio 003 - Somando dois números (Aula 01 a 06): Crie um script Python que leia dois números e tente mostrar a soma entre eles."""

# Passo 1: Criar as variáveis que irão receber os números digitados pelo usuário. Para isso, utilizar a função input() para permitir que o usuário digite os dados. Como a função input() retorna dados do tipo string por padrão, precisamos converter esses dados para realizar a soma. Para isso, usamos a função int() para converter os dados para números inteiros.

n1 = int(input('\033[1;47mDigite um valor:\n\033[m'))
n2 = int(input('\033[1;47mDigite outro valor:\n\033[m'))

# Passo 2: Com os dados das variáveis devidamente convertidos, podemos criar outra variável para armazenar a soma entre os valores usando uma expressão.

soma = n1 + n2

# Passo 3: Exibimos o resultado com a função print().

print(f'\033[mA soma entre {n1} e {n2} é igual a {soma}.\033[m')
