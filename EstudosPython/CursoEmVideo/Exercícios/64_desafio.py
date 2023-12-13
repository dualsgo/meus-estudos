# Exercício Python #064 - Tratando vários valores v1.0 - Aula 00 até 14 - Mundo 2
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0  # Inicializa o acumulador da soma
quantidade = 0  # Inicializa o contador de números digitados
condicao = True  # Inicializa a condição de repetição

while condicao:
    numero = int(input('Digite um número: [999 encerra] '))  # Solicita e converte um número para inteiro

    if numero == 999:
        print(f'Encerrando!')
        print(f'Foram digitados {quantidade} números.')
        print(f'A soma entre todos eles é {soma}.')
        condicao = False  # Altera a condição para encerrar o loop

    quantidade += 1  # Incrementa o contador de números digitados
    soma += numero  # Adiciona o número à soma total



