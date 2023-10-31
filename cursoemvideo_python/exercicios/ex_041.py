"""Desafio 041 -  (Aula 01 a 12): A CNN - Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atléta e mostre sua categoria de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER"""
print("""
    CNN - CONFEDERAÇÃO NACIONAL DE NATAÇÃO""")
# Ler o ano de nascimento
print('Digite o seu ano de nascimento: ')
ano = int(input(''))
# Categorizar
if ano <= 9:
    print('Sua categoria será: MIRIM')
elif ano <= 14:
    print('Sua categoria será: INFANTIL')
elif ano <= 19:
    print('Sua categoria será: JUNIOR')
elif ano == 20:
    print('Sua categoria será: SÊNIOR')
else:
    print('Sua categoria será: MASTER')
