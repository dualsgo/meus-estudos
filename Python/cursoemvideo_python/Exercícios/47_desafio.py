# Exercício Python #047 - Contagem de pares - Aula 00 até 13 - Mundo 2
#  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Tarefa 1: Mostrar os números pares entre 1 e 50
inicio = int(input('Digite o início do intervalo: '))  # Solicita e converte o início do intervalo para inteiro
fim = int(input('Digite o fim do intervalo: '))  # Solicita e converte o fim do intervalo para inteiro

# Para qualquer número no intervalo selecionado
print('Mostrando os números pares em verde:')
for numero in range(inicio, fim + 1):
    # Se o número for par, mostre em verde, senão, mostre em vermelho
    if numero % 2 == 0:
        print(f'\033[1;32m{numero}\033[m', end=', ')
    else:
        print(f'\033[1;31m{numero}\033[m', end=', ')

print('fim da lista.')
# Também poderíamos colocar o intervalo começando em 2 e terminando no 51, com uma iteração a cada 2 em vez de utilizar a condicional.
