"""Desafio 040 - Aquele clássico da média (Aula 01 a 12): Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de caordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média entre 7 ou superior: Aprovado
"""
# Cores
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}

# Ler duas notas de um aluno
print('Digite a sua primeira nota: ')
nota_1 = float(input(''))
print('Digite a sua segunda nota: ')
nota_2 = float(input(''))

# Calcular a média
media = (nota_1 + nota_2) / 2

# Exibir a mensagem correspondente
if media < 5:
    print(f"""{cor['red']}REPROVADO!{cor['fecha']}
{cor['destaque']}Nota corte:{cor['fecha']} {cor['red']}0 a 4.9{cor['fecha']}
{cor['destaque']}Sua média:{cor['fecha']} {cor['red']}{media:.1f}{cor['fecha']}""")
elif 7 > media >= 5:
    print(f"""{cor['yellow']}RECUPERAÇÃO!{cor['fecha']}
{cor['destaque']}Nota corte:{cor['fecha']} {cor['yellow']}5 a 6.9{cor['fecha']}
{cor['destaque']}Sua média:{cor['fecha']} {cor['yellow']}{media:.1f}{cor['fecha']}""")
else:
    print(f"""{cor['green']}APROVADO!{cor['fecha']}
{cor['destaque']}Nota corte:{cor['fecha']}: {cor['green']}7 a 10{cor['fecha']}
{cor['destaque']}Sua média:{cor['fecha']} {cor['green']}{media:.1f}{cor['fecha']}""")
