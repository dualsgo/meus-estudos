"""Desafio 057 - Validação de dados (Aula 01 a 14): Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F. Caso esteja errado peça a digitação novamente até ter um valor válido.
"""

# Solicitar o sexo
print('Digite o seu sexo: M ou F')
# A string é tratada antes para remover espaços desnecessários sendo convertida para maiúsculas
sexo = str(input('')).strip()
# Enquanto o sexo convertido para maiúsculas for diferente de F ou M
while sexo not in 'MmFf':
    # Irá exibir a mensagem de erro e soliciar que digite novamente
    print('\033[7;31;40mOpção inválida!\033[m')
    sexo = str(input('M ou F\n')).strip().upper()
# EXTRA - Converte a abreviação na palavra
if sexo.upper() == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print(f'\033[1mSeu sexo é: \033[31m{sexo}\033[m')
