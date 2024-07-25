# Exercício Python #082 - Dividindo valores em várias listas - Aula 00 até 17 - Mundo 3
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# Inicializa uma lista vazia para armazenar todos os valores digitados
lista_principal = []

# Loop principal
while True:
    # Solicita ao usuário que digite um valor
    numero = int(input('Digite um valor: '))

    if numero not in lista_principal:
        # Adiciona o valor à lista principal
        lista_principal.append(numero)
    else:
        print('Valor repetido!')

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

# Exibe as listas resultantes
print(f'A lista com todos os itens é a seguinte: {lista_principal}')

# Inicializa listas separadas para números pares e ímpares
lista_pares = []
lista_impares = []

# Classifica o valor nas listas de pares ou ímpares
for elemento in lista_principal:
    lista_pares.append(elemento) if elemento % 2 == 0 else lista_impares.append(elemento)

print(f'A lista com os elementos pares é: {lista_pares}.')
print(f'A lista com os elementos ímpares é: {lista_impares}.')
