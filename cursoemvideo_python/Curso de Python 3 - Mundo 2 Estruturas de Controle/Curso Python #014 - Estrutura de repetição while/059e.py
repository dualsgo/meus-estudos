# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

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

menu()