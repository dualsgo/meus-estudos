"""Desafio 082 -  (Aula 01 a 17): Crie um programa para ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas. AAlimentar a lista primeiro e depois fazer a análise
"""

# Criar uma lista
lista = []

# Adicionar vários números
while True:
    # Solicitar e adicionar um número à lista
    lista.append(int(input('Digite um número: ')))

    # Perguntar se deseja adicionar mais números
    pergunta = input('Adicionar mais? (S/N)').strip().upper()

    # Verificar se o comando é inválido e encerrar o loop
    if pergunta != 'S':
        print('Encerrando...')
        break

# Inicializar listas extras para valores pares e ímpares
pares = []
impares = []

# Iterar pela lista e classificar como par ou ímpar
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Exibir as três listas geradas
print(f'A lista completa é: {lista}')
print(f'A lista dos pares é: {pares}' if pares else 'Não há números pares nesta lista!')
print(f'A lista dos ímpares é: {impares}' if impares else 'Não há números ímpares nesta lista!')


