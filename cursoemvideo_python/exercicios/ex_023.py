"""Desafio 023 - Título (Aula 01 a 09): Faça um programa que leia um número entre zero e 9999 e mostre na tela cada um dos dígitos separados.

EX.: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
# FORMA DE FAZER COM DADOS DO TIPO INT

# Passo 1: Entrar com o número - O valor será armazrnado em uma variável e atribuido a ela a partir de uma função input

print('Digite um número entre 0 e 9999')
numero = int(input(''))

# Passo 2: Realizar as operações para dividir os números

# Dígitos separados
# O dígito das unidades é obtido usando o operador de módulo (%) para pegar o resto da divisão por 10.
unidade = numero % 10

# O dígito das dezenas é obtido dividindo o número por 10 e pegando o resto da divisão por 10.
dezena = (numero // 10) % 10

# O dígito das centenas é obtido dividindo o número por 100 e pegando o resto da divisão por 10.
centena = (numero // 100) % 10

# O dígito do milhar é obtido dividindo o número por 1000 e pegando o resto da divisão por 10.
milhar = (numero // 1000) % 10

# Mostrar os dígitos na tela
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')

# FORMA DE FAZER COM DADOS DO TIPO STRING

# Solicita ao usuário que digite um número
numero_str = input("Digite um número entre 0 e 9999: ")

# Garante que a string tem no máximo 4 caracteres
numero_str = numero_str[:4]

# Obtém os dígitos separados
# O dígito das unidades é o último caractere da string.
unidade = numero_str[-1]

# O dígito das dezenas é o caractere imediatamente antes das unidades.
dezena = numero_str[-2:-1]

# O dígito das centenas é o caractere antes das dezenas (ou zero, se não houver).
centena = numero_str[-3:-2] or '0'

# O dígito do milhar é o caractere antes das centenas (ou zero, se não houver).
milhar = numero_str[-4:-3] or '0'

# Mostra os dígitos na tela
print("unidade: {unidade}")
print("dezena: {dezena}")
print("centena: {centena}")
print("milhar: {milhar}")
