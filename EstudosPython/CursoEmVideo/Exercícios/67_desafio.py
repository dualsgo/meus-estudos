# Exercício Python #067 - Tabuada v3.0 - Aula 00 até 15 - Mundo 2
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
contador = 1
numero = int(input('Qual número deseja ver a tabuada?'))

while True:
    multiplo = numero * contador
    if numero < 0:
        print('Encerrando o programa...')
        break
    print(f'{numero} x {contador:2} = {multiplo:2}')
    contador += 1

    if contador == 11:
        continuar = str(input('Deseja continuar? S/N '))
        while continuar not in 'SsNn':
            print('Comando inválido')
            continuar = ''
        if continuar in 'Ss':
            numero = int(input('Tabuada de qual número? '))
            contador = 1
        if continuar in 'Nn':
            print('Ok. Encerrando...')
            break
