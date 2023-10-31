"""Desafio 042 -  (Aula 01 a 12): REFAÇA O DESAFIO 35, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero - todos os lados iguais
- Isósceles - dois lados iguais
- Escaleno - todos os lados diferentes
"""
print("""TRIÂNGULOS""")
# Coletar os lados dos triângulos
a = int(input('Digite um valor para o A lado do triângulo: '))
b = int(input('Digite um valor para o B lado do triângulo: '))
c = int(input('Digite um valor para o C lado do triângulo: '))
# A soma de dois dos três lados do triângulo deve ser maior que o terceiro lado
triangulo = a + b > c and a + c > b and b + c > a
# Verificar se os lados podem formar um triângulo. Se sim, categorizar.
if triangulo:
    print(f'Os lados {a}, {b}, {c} formam um triângulo do tipo:')
    if a == b == c:
        print('Equilátero - Todos os lados iguais.')
    elif a != b != c:
        print('Escaleno - Todos os lados diferentes')
    else:
        print('Isósceles - Dois lados iguais.')

else:
    print('Os valores para os lados que digitou não podem formar nenhum tipo de triângulo!')
