# Exercício Python #057 - Validação de Dados - Aula 00 até 14 - Mundo 2
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input('Digite o seu sexo: M/F ')).strip().upper()  # Solicita o sexo como uma string

while sexo not in 'FfMm' or sexo == '':  # Enquanto o sexo não for F ou M
    sexo = str(input('\033[1;31mSexo inválido! Digite novamente...\033[m')).strip().upper()  # Solicita o sexo como uma string

# Sendo F ou M
print('\033[1;35mSexo feminino registrado com sucesso!\033[m' if sexo == 'F' else '\033[1;34mSexo masculino registrado com sucesso!\033[m')
print('Programa finalizado!')  # Exibe mensagem de encerramento do programa


