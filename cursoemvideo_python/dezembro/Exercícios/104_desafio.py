# Exercício Python #104 - Validando entrada de dados em Python - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leia_int(mensagem):
    valor = input(mensagem)
    while not valor.isnumeric():
        print('Erro! Digite um número válido: ', end='')
        valor = input('')
    else:
        return int(valor)

numero_digitado = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {numero_digitado}.')