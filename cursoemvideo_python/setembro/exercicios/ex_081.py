"""Desafio 081 - Extraindo dados de uma lista (Aula 01 a 17): Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
- Quantos números foram digitados.
- A lista de valores ordenada de forma decrescente.
- Se o valor 5 foi digitado e está ou não na lista.
"""
# Inicializar a lista
lista = []

# Usuário digitar vários números
while True:
    elemento = int(input('Digite um valor: '))

    # Verificar se o número já está na lista
    if elemento not in lista:
        print('\033[1;32mNovo elemento adicionado!\033[m')
        lista.append(elemento)
    else:
        print('\033[1;31mElemento repetido!\033[m')

    # Perguntar se o usuário deseja adicionar mais elementos
    pergunta = input('Deseja adicionar mais elementos? (\033[1;32mS\033[m/\033[1;31mN\033[m)').strip().upper()

    # Encerrar o programa se a resposta for 'N'
    if pergunta == 'N':
        print('\033[1;31;40mPrograma encerrado!\033[m')
        break

# Exibir estatísticas da lista
print(f'Essa lista possui {len(lista)} elementos.')
print(f'Lista em ordem decrescente: {sorted(lista, reverse=True)}.')
if 5 not in lista:
    print(f'O elemento 5 não está presente na lista!')
else:
    print(f'O elemento 5 foi digitado na posição {lista.index(5)}.')

###################### Versão Guanabara

valores = []
while True:
    valores.append((int(input('Digite um valor: '))))
    resp = str(input('Quer continuar? S/N'))
    if resp in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')