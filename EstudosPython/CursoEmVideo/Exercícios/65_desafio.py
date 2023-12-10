# Exercício Python #065 - Maior e Menor valores - Aula 00 até 14 - Mundo 2
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

quantidade_de_valores = 0  # Inicializa o contador de valores
soma_valores = 0  # Inicializa o acumulador da soma dos valores
maior = menor = 0  # Inicializa as variáveis para armazenar o maior e o menor valores
continuar = True  # Inicializa a variável de continuação

while continuar:
    numero = int(input('Digite um valor: '))  # Solicita e converte um valor para inteiro
    continuar = str(input('Deseja continuar? S/N')).strip().upper()  # Pergunta se deseja continuar e converte para maiúsculas

    quantidade_de_valores += 1  # Incrementa o contador de valores
    soma_valores += numero  # Adiciona o valor à soma total

    if quantidade_de_valores == 1:
        maior = menor = numero  # Se for o primeiro valor, atribui a ele tanto o maior quanto o menor

    else:
        if numero > maior:
            maior = numero  # Atualiza o maior valor se necessário
        if numero < menor:
            menor = numero  # Atualiza o menor valor se necessário

    opcao_invalida = continuar not in 'SsNn'
    while opcao_invalida:
        print('Opção inválida!')
        continuar = str(input(''))  # Solicita novamente se a opção é inválida

    if continuar == 'S':
        print('Continuando...')
    elif continuar == 'N':
        print('Encerrando...')
        continuar = False

media_valores = soma_valores / quantidade_de_valores  # Calcula a média dos valores

print(f'Foram digitados {quantidade_de_valores} valores.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
print(f'A média entre os valores é {media_valores}')

