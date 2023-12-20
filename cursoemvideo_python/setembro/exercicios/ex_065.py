"""Desafio 065 - Maior e menor valores (Aula 01 a 14): Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
"""
# Solicitar o primeiro número ao usuário
print('Digite o primeiro número:')
numero = int(input(''))

contador = 1
acumulador = numero
maior = numero  # Inicializar maior e menor com o primeiro número
menor = numero

continuar = str(input('Deseja continuar? S/N')).strip().upper()

while continuar in 'N':
    if continuar in 'S':
        print('Certo! Vamos continuar'
              '...')
        numero = int(input('Digite o próximo número: '))
        acumulador += numero  # Acumular os valores
        contador += 1
        if numero > maior:
            maior = numero  # Atualizar o maior número se necessário
        elif numero < menor:
            menor = numero  # Atualizar o menor número se necessário
        continuar = str(input('Deseja continuar? S/N')).strip().upper()
    else:
        print('Ok, até a próxima!')
        continuar = 'N'

if contador > 0:  # Verificar se pelo menos um número foi inserido para evitar divisão por zero
    print(f'Você digitou {contador} valores.')
    print(f'A média entre os valores fornecidos é {acumulador / contador}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
else:
    print('Nenhum número foi fornecido.')

