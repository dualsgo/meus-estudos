# Exercício Python #067 - Tabuada v3.0 - Aula 00 até 15 - Mundo 2
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    try:
        valor = int(input('Tabuada de qual valor? '))
        while True:
            for i in range(1, 11):
                print(f'{valor:2} X {i:2} = {valor*i:3}')
            valor = int(input('Qual o próximo valor? '))
            if valor < 0:
                break
        print(f'Encerrando o programa!')
        break
    except ValueError:
        print(f'Valor de um tipo inválido para essa operação.')


