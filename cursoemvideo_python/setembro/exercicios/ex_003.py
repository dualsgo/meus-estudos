""" Desafio 003 - Somando dois números (Aula 01 a 06): Crie um script Python que leia dois números e tente mostrar a soma entre eles."""

# Passo 1: Criar as variáveis que irão receber os números digitados pelo usuário. Para isso, utilizar a função input() para permitir que o usuário digite os dados. Como a função input() retorna dados do tipo string por padrão, precisamos converter esses dados para realizar a soma. Para isso, usamos a função int() para converter os dados para números inteiros.

n1 = int(input('\033[1;47mDigite um valor:\033[m\n'))
n2 = int(input('\033[1;47mDigite outro valor:\033[m\n'))

# Passo 2: Com os dados das variáveis devidamente convertidos, podemos criar outra variável para armazenar a soma entre os valores usando uma expressão.

soma = n1 + n2

# Passo 3: Exibimos o resultado com a função print().

print(f'\033[1mA soma entre \033[31m{n1}\033[m \033[1me\033[m \033[1;31m{n2}\033[m \033[1mé igual a\033[m \033[1;32m{soma}\033[m.\033[m')
