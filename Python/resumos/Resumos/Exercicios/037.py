# Exercício Python #037 - Conversor de Bases Numéricas
# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

while True:
    try:
        valor = int(input('Digite um valor: '))
        escolha = int(input('Escolha a base:\n[1] Binária [2] Octal [3] Hexadecimal: '))
        if escolha == 1:
            convertido = f'{valor:b}'
            base = 'binária'
        elif escolha == 2:
            convertido = f'{valor:o}'
            base = 'octal'
        elif escolha == 3:
            convertido = f'{valor:x}'
            base = 'hexadecimal'
        else:
            print('Escolha inválida.')
            continue  # Volta ao início do loop para pedir um novo valor
        print(f'O número {valor} na base {base} é {convertido}')
        break
    except ValueError:
        print('Valor inválido para essa operação. Tente novamente.')