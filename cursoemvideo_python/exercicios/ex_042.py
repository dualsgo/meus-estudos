"""Desafio 042 - Analisando triângulos v2.0 (Aula 01 a 12): REFAÇA O DESAFIO 35, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero - todos os lados iguais
- Isósceles - dois lados iguais
- Escaleno - todos os lados diferentes
"""
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}
print(f"""{cor['destaque']}TRIÂNGULOS{cor['fecha']}""")
# Coletar os lados dos triângulos
a = int(input('Digite um valor para o lado A do triângulo: '))
b = int(input('Digite um valor para o lado B do triângulo: '))
c = int(input('Digite um valor para o lado C do triângulo: '))
# A soma de dois dos três lados do triângulo deve ser maior que o terceiro lado
triangulo = a + b > c and a + c > b and b + c > a
# Verificar se os lados podem formar um triângulo. Se sim, categorizar.
if triangulo:
    print(f'{cor["destaque"]}Os lados {a}, {b}, {c} formam um triângulo do tipo:{cor["fecha"]}')
    if a == b == c:
        print(f'{cor["green"]}Equilátero - Todos os lados iguais.{cor["fecha"]}')
    elif a != b != c != a:
        print(f'{cor["yellow"]}Escaleno - Todos os lados diferentes{cor["fecha"]}')
    else:
        print(f'{cor["red"]}Isósceles - Dois lados iguais.{cor["fecha"]}')
else:
    print('Os valores para os lados que digitou não podem formar nenhum tipo de triângulo!')
