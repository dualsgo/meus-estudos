# Exercício Python #066 - Vários números com flag - Aula 00 até 15 - Mundo 2
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando a flag).

soma = 0  # Inicializa a variável que irá armazenar a soma dos números digitados
quantidade = 0  # Inicializa a variável que irá contar a quantidade de números digitados

# Loop principal para receber valores do usuário
while True:
    numero = int(input('Digite um valor: [999 encerra] '))

    if numero == 999:
        break  # Se o número digitado for 999, encerra o loop

    soma += numero  # Adiciona o número à soma acumulada
    quantidade += 1  # Incrementa a quantidade de números digitados

# Exibe o resultado
print(f'A soma entre todos os {quantidade} números digitados é {soma}.')
