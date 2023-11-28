# Exercício Python #004 - Dissecando uma Variável - Aula 00 até 06
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Tarefa 1: Ler algo pelo teclado.
algo = input('Digite algo: ')

# Tarefa 2: Mostrar na tela o seu tipo primitivo e outras informações.
print(f'O tipo primitivo desse valor é {type(algo)}.')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um numérico (contém somente números)? {algo.isnumeric()}')
print(f'É alfabético (contém somente letras)? {algo.isalpha()}')
print(f'É alfanumérico (contém letras ou números)? {algo.isalnum()}')
print(f'Está todo em MAIÚSCULAS? {algo.isupper()}')
print(f'Está todo em minúsculas? {algo.islower()}')
print(f'Está capitalizado (somente a primeira letra maiúscula)? {algo.istitle()}')

'''Todo objeto tem características e e realiza funcionalidades (atributos e métodos). Todos os métodos terminam com parênteses.'''

