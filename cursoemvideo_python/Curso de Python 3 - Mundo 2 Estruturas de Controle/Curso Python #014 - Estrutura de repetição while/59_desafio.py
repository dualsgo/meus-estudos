# Exercício Python #059 - Criando um Menu de Opções - Aula 00 até 14 - Mundo 2
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from emoji import emojize
continuar = True  # Inicializa a variável de controle para continuar o programa

print(emojize('Aplicativos :telefone_celular:', language='pt'))
primeiro_numero = int(input(emojize(':teclado: Escolha o primeiro número: ', language='pt')))  # Solicita e converte o primeiro número para inteiro
segundo_numero = int(input(emojize(':teclado: Escolha o segundo número: ', language='pt')))  # Solicita e converte o segundo número para inteiro
while continuar:
    print(emojize('Escolha uma das opções:\n:tecla_1: Somar :símbolo_de_adição:\n:tecla_2: Multiplicar :sinal_de_multiplicação:\n:tecla_3: Maior :régua_reta:\n:tecla_4: Novos números :teclado:\n:tecla_5: Sair do programa :botão_ejetar:', language='pt'))
    escolha = int(input(''))  # Solicita e converte a escolha para inteiro
    resultado = 0

    if escolha == 1:
        print(emojize(':símbolo_de_adição: Somando', language='pt'))
        resultado = primeiro_numero + segundo_numero
        print(f'\033[7;30;47mA soma entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 2:
        print(emojize(':sinal_de_multiplicação: Multiplicando', language='pt'))
        resultado = primeiro_numero * segundo_numero
        print(f'\033[7;30;47mO produto entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 3:
        print(emojize(':régua_reta: Maior entre eles', language='pt'))
        if primeiro_numero == segundo_numero:
            print('\033[7;30;47mOs números são iguais!\033[m')
        else:
            resultado = primeiro_numero if primeiro_numero > segundo_numero else segundo_numero
            print(f'\033[7;30;47mEntre {primeiro_numero} e {segundo_numero}, {resultado} é o maior!\033[m')

    elif escolha == 4:
        print('Escolha novos números:')
        primeiro_numero = int(input(''))  # Solicita e converte o novo primeiro número para inteiro
        segundo_numero = int(input(''))  # Solicita e converte o novo segundo número para inteiro

    elif escolha == 5:
        print('\033[1;41mEncerrando...\033[m')
        continuar = False

    else:
        print('Escolha inválida!')

    if escolha:
        continuar = input('Continuar? S/N').strip().upper()  # Solicita se o usuário deseja continuar
        if continuar == 'N':
            continuar = False
        elif continuar != 'S':
            print('Comando inválido!')
            continuar = input('S/N').strip().upper()

print('Programa finalizado!')  # Exibe mensagem de encerramento do programa

"""# VERSÃO 2

from emoji import emojize

continuar = True  # Inicializa a variável de controle para continuar o programa

print(emojize('Aplicativos :telefone_celular:', language='pt'))

primeiro_numero = int(input(emojize(':teclado: Escolha o primeiro número: ', language='pt')))
# Solicita e converte o primeiro número para inteiro

segundo_numero = int(input(emojize(':teclado: Escolha o segundo número: ', language='pt')))
# Solicita e converte o segundo número para inteiro


while continuar:
    print(emojize('Escolha uma das opções:\n:tecla_1: Somar :símbolo_de_adição:\n:tecla_2: Multiplicar :sinal_de_multiplicação:\n:tecla_3: Maior :régua_reta:\n:tecla_4: Novos números :teclado:\n:tecla_5: Sair do programa :botão_ejetar:', language='pt'))

    escolha = int(input(''))  # Solicita e converte a escolha para inteiro
    resultado = 0

    if escolha == 1:
        print(emojize(':símbolo_de_adição: Somando', language='pt'))
        resultado = primeiro_numero + segundo_numero
        print(f'\033[7;30;47mA soma entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 2:
        print(emojize(':sinal_de_multiplicação: Multiplicando', language='pt'))
        resultado = primeiro_numero * segundo_numero
        print(f'\033[7;30;47mO produto entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 3:
        print(emojize(':régua_reta: Maior entre eles', language='pt'))
        if primeiro_numero == segundo_numero:
            print('\033[7;30;47mOs números são iguais!\033[m')
        else:
            resultado = primeiro_numero if primeiro_numero > segundo_numero else segundo_numero
            print(f'\033[7;30;47mEntre {primeiro_numero} e {segundo_numero}, {resultado} é o maior!\033[m')

    elif escolha == 4:
        print('Escolha novos números:')
        primeiro_numero = int(input(''))  # Solicita e converte o novo primeiro número para inteiro
        segundo_numero = int(input(''))  # Solicita e converte o novo segundo número para inteiro

    elif escolha == 5:
        print('\033[1;41mEncerrando...\033[m')
        continuar = False

    else:
        print('Escolha inválida!')

    if escolha:
        continuar = input('Continuar? S/N').strip().upper()  # Solicita se o usuário deseja continuar
        if continuar == 'N':
            continuar = False
        elif continuar != 'S':
            print('Comando inválido!')
            continuar = input('S/N').strip().upper()

print('Programa finalizado!')  # Exibe mensagem de encerramento do programa

# VERÃO 3

def continuar():
    pergunta = input('Deseja continuar? [S] ou [N] ').upper().strip()
    while pergunta not in 'SN':
        print('Digite S para continuar ou N para encerrar')
        pergunta = input('... ').strip().upper()
    if pergunta == 'S':
        return 0
    elif pergunta == 'N':
        return 5

def obter_valores(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Este valor não é válido para essa operação.')

def menu():
    opções = [1, 2, 3, 4, 5]
    opção = 0
    while opção != 5:
        try:
            print('-'*50)
            print('Digite o número correspondente à opção desejada:'.center(50))
            print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
            print('-'*50)

            opção = int(input('Sua escolha foi: '))
            if opção == 1:
                print('-' * 50)
                print('Somar dois valores'.center(50))
                print('-' * 50)
                valor1 = obter_valores('Digite o primeiro valor: ')
                valor2 = obter_valores('Digite o segundo valor: ')
                resultado = valor1 + valor2
                print('Seu resultado:'.center(50))
                print(f'{valor1} + {valor2} = {resultado}')
                print('-' * 50)
                opção = continuar()

            elif opção == 2:
                print('-' * 50)
                print('Multiplicar dois valores'.center(50))
                print('-' * 50)
                valor1 = obter_valores('Digite o primeiro valor: ')
                valor2 = obter_valores('Digite o segundo valor: ')
                resultado = valor1 * valor2
                print('Seu resultado:'.center(50))
                print(f'{valor1} x {valor2} = {resultado}')
                print('-' * 50)
                opção = continuar()

            elif opção == 3:
                print('-' * 50)
                print('Comparar dois valores'.center(50))
                print('-' * 50)
                valor1 = obter_valores('Digite o primeiro valor: ')
                valor2 = obter_valores('Digite o segundo valor: ')
                print('-' * 50)
                print('Seu resultado:'.center(50))
                if valor1 == valor2:
                    print('Valores iguais!')
                else:
                    resultado = valor1 if valor1 > valor2 else valor2
                    print(f'Menor: {min(valor1, valor2)}, Maior: {max(valor1, valor2)} | O maior é {resultado}')
                print('-' * 50)
                opção = continuar()

            elif opção == 4:
                print('-' * 50)
                print('Digitar novos valores'.center(50))
                print('Primeiro escolha a operação')
                print('-' * 50)
                opção = 0

            elif opção == 5:
                break

        except ValueError:
            print('O valor digitado não é válido para essa operação. Tente novamente.')

    print('-' * 50)
    print('Operação encerrada!')
    print('-' * 50)

while menu() != 5:
    menu()"""