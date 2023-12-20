# Exercício Python #081 - Extraindo dados de uma Lista - Aula 00 até 17 - Mundo 3
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# Inicializa uma lista vazia
lista = []

# Inicializa um contador para o número de itens na lista
contador = 0

# Loop principal
while True:
    # Solicita ao usuário que digite um valor
    numero = int(input('Digite um valor: '))

    # Adiciona o valor à lista
    lista.append(numero)

    # Incrementa o contador
    contador += 1

    # Pergunta ao usuário se deseja continuar
    continuar = str(input('Deseja continuar? S/N ')).strip().upper()

    # Valida a resposta do usuário
    while continuar not in 'SsNn':
        print('Comando inválido!')
        continuar = str(input('Deseja continuar? S/N ')).strip().upper()

    # Verifica se o usuário deseja continuar
    if continuar in 'S':
        print('Continuando...')
    elif continuar in 'N':
        print('Finalizando...')
        break

# Exibe o número de itens na lista
print(f'Foram digitados {contador} itens na lista!')

# Ordena a lista em ordem decrescente
lista.sort(reverse=True)

# Exibe a lista ordenada
print(f'A lista em ordem decrescente é a seguinte: {lista}')

# Verifica se o valor 5 está presente na lista
print(f'O valor 5 foi digitado e está na lista.' if 5 in lista else 'O valor 5 não foi digitado e não está presente na lista.')


