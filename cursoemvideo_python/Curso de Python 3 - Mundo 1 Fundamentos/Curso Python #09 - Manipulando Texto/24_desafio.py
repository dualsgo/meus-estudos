# Exercício Python #024 - Verificando as primeiras letras de um texto - Aulas 00 até 09 - Mundo 1
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

# Tarefa 1: Ler o nome de uma cidade.
cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()

# Tarefa 2: Verificar se começa ou não com 'SANTO'
if cidade[:5] == 'SANTO':
    print(f'A cidade {cidade} começa com SANTO!')
else:
    print(f'A cidade {cidade} não começa com SANTO, e sim com {cidade[:5]}.')


# Versão 2

print('\033[1;32mComeça com Santo."\033[m' if input('Digite o nome da cidade: ').strip().title().split()[0] == 'Santo' else '\033[1;31mNão começa com "Santo"\033[m')

print('\033[1;32mComeça com "Santo"\033[m' if input('Nome da cidade: ').strip().title().startswith('Santo') else '\033[1;31mNão começa com "Santo"\033[m')