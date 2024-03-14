# Exercício Python #042 - Analisando Triângulos v2.0 - Aula 00 até 12 - Mundo 2
# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

# Tarefa 1: Ler três retas
a = int(input('Digite o valor do segmento A: '))
b = int(input('Digite o valor do segmento B: '))
c = int(input('Digite o valor do segmento C: '))

# Tarefa 2: Avaliar se formam um triângulo
print('\033[1;32mPara que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois\033[m')
triangulo = a < b + c and c < b + a and b < a + c
print(triangulo)
print(f'\033[1mA {a} < B {b} + C {c}')
print(f'B {b} < C {c} + A {a}')
print(f'C {c} < A {a} + B {b}\033[m\n')

# Tarefa 2: Definir as condições para cada topo de triângulo

# EQUILÁTERO: todos os lados iguais
equilatero = a == b == c == a
# ESCALENO: todos os lados diferentes
escaleno = a != b != c != a
# ISÓSCELES: dois lados iguais, um diferente
isosceles = not equilatero and not escaleno
# Tarefa 3: Mostrar se forma um triângulo e de qual tipo

if triangulo:
    print(f'\033[1mOs segmentos de comprimento a = {a}, b = {b} e c = {c} podem formar um\033[m', end=' ')
    if equilatero:
        print('\033[1;31mTRIÂNGULO EQUILÁTERO - TODOS OS LADOS IGUAIS\033[m')
    elif escaleno:
        print('\033[1;31mTRIÂNGULO ESCALENO - TODOS OS LADOS DIFERENTES\033[m')
    elif isosceles:
        print('\033[1;31mTRIÂNGULO ISÓSCELES - DOIS LADOS IGUAIS E UM DIFERENTE\033[m')
else:
    print(f'Não é possível formar um triângulo com os segmentos a = {a}, b = {b} e c = {c}.')

