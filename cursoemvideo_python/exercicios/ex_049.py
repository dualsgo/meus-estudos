"""Desafio 049 - Tabuada V.2.0 (Aula 01 a 13): Refaça o exercício do desafio 9 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando laço for."""

# Recebemos o fator
fator = int(input('Digite um número para saber a tabuada: '))
# Exibimos uma mensagem
print(f'A tabuada de {fator} é:')
# Criamos o laço no intervalo de 1 a 10
for i in range(1, 11):
    print(f'\033[32m{fator}\033[m x\033[32m {i}\033[m = \033[31m{fator * i}\033[m')
print('FIM!')