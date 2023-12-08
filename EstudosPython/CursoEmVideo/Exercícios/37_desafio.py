# Exercício Python #037 - Conversor de Bases Numéricas - Aula 00 até 12 - Mundo 2
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Tarefa 1: Ler um número inteiro
numero = int(input('Digite um número: '))
print('[1] BINARIO\n[2] OCTAL\n[3] HEXADECIMAL')
escolha = int(input('>>> '))
conversao = 0
if 0 > numero < 4:
    print(f'O número {numero} em', end=' ')
# Tarefa 2: Configurar as conversões
if escolha == 1:
    print('BINÁRIO', end=' ')
    conversao = bin(numero)[2:]
elif escolha == 2:
    print('OCTAL', end=' ')
    conversao = oct(numero)[2:]
elif escolha == 3:
    print('HEXADECIMAL', end=' ')
    conversao = hex(numero)[2:]
else:
    print('Opção inválida. Encerrando...')

# Tarefa 3: Escolher a base de conversão e exibir o resultado
if 0 > numero < 4:
    print(f'é igual a {conversao}')
