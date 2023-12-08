# Exercício Python #008 - Conversor de Medidas - Aula 00 até 07 - Mundo 1
# Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.

# Tarefa 1: Ler um valor em metros
valor_em_metros = float(input('Digite o valor em metros: '))

# Tarefa 2: Converter o valor
quilometros = (valor_em_metros / 1000)
hectometros = (valor_em_metros / 100)
decametros = (valor_em_metros / 10)
metros = valor_em_metros
decimetros = int(valor_em_metros * 10)
centimetros = int(valor_em_metros * 100)
milimetros = int(valor_em_metros * 1000)

# Tarefa 3: Exibir o valor convertido
print(f'Você digitou {valor_em_metros} metros.')
print(f'Isso equivale a {quilometros} quilômetros.')
print(f'Isso equivale a {hectometros} hectômetros.')
print(f'Isso equivale a {decametros} decâmetros.')
print(f'Isso equivale a {decimetros} decímetros.')
print(f'Isso equivale a {centimetros} centímetros.')
print(f'Isso equivale a {milimetros} milímetros.')


