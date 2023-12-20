"""Desafio 085 -  (Aula 01 a 18): Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
# Inicializar as listas
lista = list()  # Lista principal para receber as sub-listas
pares = list()  # Sub-lista de números pares
impares = list()  # Sub-lista de números ímpares

# Receber 7 números digitados pelo usuário
for numero in range(7):
    while True:
        # Solicitar ao usuário para digitar um número
        valor = int(input(f'Digite o \033[1;34m{numero+1}º\033[m valor: '))

        # Verificar se o valor já foi inserido em pares ou impares
        if valor in pares or valor in impares:
            print('Valor repetido! Digite outro.')
        else:
            # Se o valor for único, sair do loop
            break

    # Classificar o número nas sub-listas correspondentes
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Ao fim do loop, adiciona as sub-listas à lista principal
lista.append(pares[:])
lista.append(impares[:])

# Exibir os resultados
print(f'A lista completa é: \033[1;34m{sorted(lista)}\033[m')
print(f'A lista de pares é: \033[1;31m{sorted(pares)}\033[m')
print(f'A lista de ímpares é: \033[1;32m{sorted(impares)}\033[m')



