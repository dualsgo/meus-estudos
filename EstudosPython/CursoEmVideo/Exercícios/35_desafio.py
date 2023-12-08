# Exercício Python #035 - Analisando Triângulo v1.0 - Aula 00 até 09 - Mundo 1
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# b + c > a
from random import randint
# Tarefa 1: Ler três retas
a = randint(1, 99)
b = randint(1, 99)
c = randint(1, 99)

# Tarefa 2: Avaliar se formam um triângulo
print('Para que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois')
triangulo = b + c > a and b + a > c and a + c > b

print(f'A {a} + B {b} > C {c}')
print(f'B {b} + C {c} > A {a}')
print(f'C {c} + A {a} > B {b}')

if triangulo:
    print(f'Os segmentos de comprimento a={a}, b={b} e c={c} podem formar um triângulo!')
else:
    print(f'Não é possível formar um triângulo com os segmentos a={a}, b={b} e c={c}.')