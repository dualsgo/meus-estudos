"""Desafio 023 - Separando dígitos de um número (Aula 01 a 09): Faça um programa que leia um número entre zero e 9999 e mostre na tela cada um dos dígitos separados.

EX.: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
# FORMA DE FAZER COM DADOS DO TIPO INT

# Passo 1: Entrar com o número - O valor será armazenado em uma variável e atribuido a ela a partir de uma função input()

print("""
# MÉTODO 1: EM FORMATO NUMÉRICO #
\033[1mDigite um número entre 0 e 9999:\033[m""")
numero = int(input(''))

# Passo 2: Realizar as operações para dividir os números

# Dígitos separados - Para a unidade basta usar o resto da divisão do número digitado por 10. Assim o resultado sempre será alguma unidade já que qualquer divisão por 10 só é possível com números terminados em zero

# Para as dezenas, centenas e milhar, basta antes realizar a divisão exata por 10, 100 ou 1000. Pois nessa divisão por multiplos de 10 basta mover a vírgula para a esquerda tantas vezes quanto a quantidade de zeros do divisor. Depois fazemos o resto da divisão para retornar o algarirsmo que estiver na primeira posição a esquerda da virgura

# O dígito das unidades é obtido usando o operador de módulo (%) para pegar o resto da divisão por 10.
unidade = numero % 10

# O dígito das dezenas é obtido dividindo o número por 10 e pegando o resto da divisão por 10.
dezena = (numero // 10) % 10

# O dígito das centenas é obtido dividindo o número por 100 e pegando o resto da divisão por 10.
centena = (numero // 100) % 10

# O dígito do milhar é obtido dividindo o número por 1000 e pegando o resto da divisão por 10.
milhar = (numero // 1000) % 10

# Mostrar os dígitos na tela
print(f'\033[1;31munidade: {unidade}\033[m')
print(f'\033[1;31mdezena: {dezena}\033[m')
print(f'\033[1;31mcentena: {centena}\033[m')
print(f'\033[1;31mmilhar: {milhar}\033[m')

# FORMA DE FAZER COM DADOS DO TIPO STRING

# Solicita ao usuário que digite um número
numero_str = input("""MÉTODO 2: FORMATO DE STRING
\033[1mDigite um número entre 0 e 9999: \033[1m""")

# Garante que a string tem no máximo 4 caracteres
numero_str = numero_str[:4]

# Obtém os dígitos separados
# O dígito das unidades é o último caractere da string.
unidade = numero_str[-1]

# O dígito das dezenas é o caractere imediatamente antes das unidades.
dezena = numero_str[-2:-1] or '0'

# O dígito das centenas é o caractere antes das dezenas (ou zero, se não houver).
centena = numero_str[-3:-2] or '0'

# O dígito do milhar é o caractere antes das centenas (ou zero, se não houver).
milhar = numero_str[-4:-3] or '0'

# Mostra os dígitos na tela
print(f"\033[1;32munidade: {unidade}\033[m")
print(f"\033[1;32mdezena: {dezena}\033[m")
print(f"\033[1;32mcentena: {centena}\033[m")
print(f"\033[1;32mmilhar: {milhar}\033[m")
