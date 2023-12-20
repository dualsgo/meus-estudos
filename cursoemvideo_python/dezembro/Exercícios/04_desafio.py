# Exercício Python #004 - Dissecando uma Variável - Aula 00 até 06 - Mundo 1
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Tarefa 1: Ler algo pelo teclado.
algo = input('Digite algo: ') # Nesse exercício nos limitamos a strings, pois é o valor padrão retornado pelo input()

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

def sim_ou_nao(condicao):
    return 'Sim' if condicao else 'Não'

algo = input('Digite algo: ')

print(f'O valor digitado é do tipo {type(algo).__name__} e contém a seguinte informação: {algo}')
# Verifica se só tem espaços em branco
print(f'Só tem espaços? {sim_ou_nao(algo.isspace())}')
# Verifica se é um numérico (contém somente números)
print(f'É um numérico (contém somente números)? {sim_ou_nao(algo.isnumeric())}')
# Verifica se é alfabético (contém somente letras)
print(f'É alfabético (contém somente letras)? {sim_ou_nao(algo.isalpha())}')
# Verifica se é alfanumérico (contém letras ou números)
print(f'É alfanumérico (contém letras ou números)? {sim_ou_nao(algo.isalnum())}')
# Verifica se está todo em MAIÚSCULAS
print(f'Está todo em MAIÚSCULAS? {sim_ou_nao(algo.isupper())}')
# Verifica se está todo em minúsculas
print(f'Está todo em minúsculas? {sim_ou_nao(algo.islower())}')
# Verifica se está capitalizado (somente a primeira letra maiúscula)
print(f'Está capitalizado (somente a primeira letra maiúscula)? {sim_ou_nao(algo.istitle())}')

