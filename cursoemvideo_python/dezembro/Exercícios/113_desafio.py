# Exercício Python #113 - Funções aprofundadas em Python - Aula 00 até 23 - Mundo 3
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leia_int(msg):
    while True:
        try:
            msg = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido...')
            continue
        except KeyboardInterrupt:
            print(f'Programa foi interrompido!')
            msg = ''
        else:
            return msg

def leia_float(msg):
    while True:
        try:
            msg = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido...')
            continue
        except KeyboardInterrupt:
            print(f'Programa foi interrompido!')
            msg = ''
        else:
            return msg


numero = leia_int('Digite um número inteiro: ')
num = leia_float('Digite um número float: ')


print(f'Você digitou o número INTEIRO {numero}')
print(f'Você digitou o número FLOAT {num}')