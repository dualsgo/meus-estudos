"""Desafio 014 - Conversor de temperaturas (Aula 00 a 00): Escreva um programa que converta uma temperatura digitada em C e converta para F."""

# Passo 1: Ler a temperatura em Celcius -
print("""
\033[1;41mQUENTE\033[m OU \033[1;44mFRIO\033[m ?\n""")
print('Digite a temperatura em ° C:')
c = float(input(''))
# Passo 2: Converter e exibir a temperatura em Fahrenheit
# Uitilizando parenteses para deixar mais clara a ordem de precedência
f = (c * (9/5)) + 32

print(f'{c:.1f} ° C equivalem a {f:.1f} ° F.')
