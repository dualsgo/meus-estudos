# Curso Python #22 - Módulos e Pacotes

# Modularização:
# Surgiu no início da década de 60
# Sistemas ficando cada vez maiores
# Foco: dividir um programa grande
# Foco: aumentar a legibilidade
# Foco: facilitar a manutenção

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    return n * 2


def triplo(n):
    return n * 3