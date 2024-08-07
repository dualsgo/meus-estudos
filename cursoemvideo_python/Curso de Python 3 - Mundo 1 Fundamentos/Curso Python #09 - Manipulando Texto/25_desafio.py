# Exercício Python #025 - Procurando uma string dentro de outra - Aulas 00 até 09 - Mundo 1
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.4

# Tarefa 1: Ler o nome de uma pessoa
nome = str(input('Digite um nome: ')).strip().upper()

# Tarefa 2: Verificar se ha´silva no nome
if 'SILVA' in nome:
    print(f'SILVA está presente no nome {nome}.')
else:
    print(f'SILVA não está presente no nome {nome}.')
    
# Versão 2 - Simplificada

print(f'\033[1;32mContém "Silva"\033[m' if 'Silva' in input('Digite seu nome completo: ') else '\033[1;31mNão contém "Silva"\033[m')