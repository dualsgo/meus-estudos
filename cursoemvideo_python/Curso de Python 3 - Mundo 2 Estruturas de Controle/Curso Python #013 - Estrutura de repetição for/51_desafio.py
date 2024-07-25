# Exercício Python #051 - Progressão Aritmética - Aula 00 até 13 - Mundo 2
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Tarefa 1: Ler o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))  # Solicita e converte o primeiro termo para inteiro
razao = int(input('Digite a razão da PA: '))  # Solicita e converte a razão para inteiro
dez_primeiros = 10 * razao  # Calcula o décimo termo (posição 10) da PA

# Tarefa 2: Mostrar os 10 primeiros termos
print(f'Os dez primeiros termos da PA são: ', end='')
for termo in range(primeiro_termo, dez_primeiros, razao):
    print(f'{termo}', end=', ')  # Exibe cada termo seguido de uma vírgula
print('FIM!')  # Indica o final da lista

