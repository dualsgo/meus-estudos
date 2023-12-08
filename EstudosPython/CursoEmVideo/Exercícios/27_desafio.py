# Exercício Python #027 - Primeiro e último nome de uma pessoa - Aulas 00 até 09 - Mundo 1
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Tarefa 1: Ler o nome completo pelo teclado
nome = str(input('Digite o seu nome completo: ')).strip().upper()

# Tarefa 2: Mostrar o primeiro e o último nome separadamente
nome_separado = nome.split()

# Primeiro nome
primeiro_nome = nome_separado[0]
print(f'O primeiro nome é {primeiro_nome}.')

# Ultimo nome
ultimo_nome = nome_separado[-1]
print(f'O último nome é {ultimo_nome}.')