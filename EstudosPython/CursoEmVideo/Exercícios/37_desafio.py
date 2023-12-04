# Exercício Python #037 - Conversor de Bases Numéricas
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Tarefa 1: Ler um número inteiro
numero = int(input('Digite um número: '))
print('[1] BINARIO [2] OCTAL [3] HEXADECIMAL')
escolha = int(input(''))
print(f'O número {numero} em', end=' ')
convertidos = ''
# Tarefa 2: Configurar as conversões
if escolha == 1:
    print('BINÁRIO', end=' ')
    convertidos = str(bin(numero))
elif escolha == 2:
    print('OCTAL', end=' ')
    convertidos = str(oct(numero))
elif escolha == 3:
    print('HEXADECIMAL', end=' ')
    convertidos = str(hex(numero))
else:
    print('Opção inválida. Encerrando...')

# Tarefa 3: Escolher a base de conversão e exibir o resultado
print(f'é igual a {convertidos[2:]}')
