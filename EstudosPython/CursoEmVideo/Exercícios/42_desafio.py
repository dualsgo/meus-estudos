# Exercício Python #042 - Analisando Triângulos v2.0
# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

# Tarefa 1: Verificar se os segmentos formam um triângulo
# Ler três retas
a = int(input('Digite o valor do segmento A'))
b = int(input('Digite o valor do segmento B'))
c = int(input('Digite o valor do segmento C'))

# Tarefa 2: Avaliar se formam um triângulo
print('Para que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois')
triangulo = b + c > a and b + a > c and a + c > b

print(f'A {a} + B {b} > C {c}')
print(f'B {b} + C {c} > A {a}')
print(f'C {c} + A {a} > B {b}')
# Tarefa 2: Definir as condições para cada topo de triângulo

# EQUILÁTERO: todos os lados iguais
equilatero = a == b == c
# ESCALENO: todos os lados diferentes
escaleno = a != b != c
# ISÓSCELES: dois lados iguais, um diferente
isosceles = not equilatero and not escaleno
# Tarefa 3: Mostrar se forma um triângulo e de qual tipo

if triangulo:
    print(f'Os segmentos de comprimento a={a}, b={b} e c={c} podem formar um', end=' ')
    if equilatero:
        print('TRIâNGULO EQUILÁTERO - TODOS OS LADOS IGUAIS')
    elif escaleno:
        print('TRIÂNGULO ESCALENO - TODOS OS LADOS DIFERENTES')
    elif isosceles:
        print('TRIÂNGULO ISÓSCELES - DOIS LADOS IGUAIS E UM DIFERENTE')
else:
    print(f'Não é possível formar um triângulo com os segmentos a={a}, b={b} e c={c}.')

