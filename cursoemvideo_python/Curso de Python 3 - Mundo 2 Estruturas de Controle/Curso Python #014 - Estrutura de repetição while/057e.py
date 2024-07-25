# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo: M ou F ').upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = input('Sexo inválido. Digite novamente: M ou F ').upper().strip()

print(f'Sexo: {"Masculino" if sexo == "M" else "Feminino"}')