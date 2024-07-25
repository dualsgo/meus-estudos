# Exercício Python #065 - Maior e Menor valores
# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


valores = []
while True:
    try:
        valor = int(input('Digite um valor: '))
        valores.append(valor)
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')
        continue

    while True:
        continuar = input('Deseja continuar? (S/N): ').strip().upper()
        if continuar not in ('S', 'N'):
            print('Resposta inválida. Por favor, digite S ou N.')
        else:
            break

    if continuar == 'N':
        break

if valores:
    print(f'A média entre todos os {len(valores)} valores digitados é {sum(valores) / len(valores)}')
    print(f'O maior valor digitado foi {max(valores)}, enquanto o menor foi {min(valores)}.')
else:
    print('Nenhum valor foi digitado.')