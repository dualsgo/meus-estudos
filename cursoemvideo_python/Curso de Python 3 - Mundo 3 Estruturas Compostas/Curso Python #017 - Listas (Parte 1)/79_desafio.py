# Exercício Python #079 - Valores únicos em uma Lista - Aula 00 até 17 - Mundo 3
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Inicializa uma lista vazia para armazenar os valores inseridos pelo usuário
lista = []

# Loop infinito para permitir a adição contínua de valores
while True:
    # Solicita ao usuário que digite um valor inteiro
    valor = int(input('Digite um valor: '))

    # Verifica se o valor já está na lista
    if valor not in lista:
        # Adiciona o valor à lista se ainda não estiver presente
        lista.append(valor)
        print('\033[1;32mValor adicionado!\033[m')  # Mensagem de confirmação em verde
    else:
        print('\033[1;31mValor repetido!\033[m')  # Mensagem de aviso em vermelho se o valor já estiver na lista

    # Pergunta ao usuário se deseja adicionar mais valores
    continuar = str(input('Adicionar mais valores? S/N ')).strip().upper()

    # Verifica se a resposta é válida (S ou N)
    if continuar in 'SN':
        # Se for 'S', continua o loop
        if continuar == 'S':
            print('Continuando...')
        # Se for 'N', encerra o loop
        else:
            print('Encerrando...')
            # Ordena a lista e sai do loop
            lista.sort()
            break

# Imprime os valores adicionados à lista após o encerramento do loop
print(f'Os valores adicionados foram: {lista}')
