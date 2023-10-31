"""Desafio 040 -  (Aula 01 a 12): Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de caordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média entre 7 ou superior: Aprovado
"""

# Ler duas notas de um aluno
print('Digite a sua primeira nota: ')
nota_1 = float(input(''))
print('Digite a sua segunda nota: ')
nota_2 = float(input(''))
# Calcular a média
media = (nota_1 + nota_2) / 2
# Exibir a mensagem correspondente
if media < 5:
    print(f"""REPROVADO!
Nota corte: 0 a 4.9
Sua média {media:.1f}.""")
elif media >= 5 and media < 7:
    print(f"""RECUPERAÇÃO!
Nota corte: 5 a 6.9
Sua média {media:.1f}.""")
else:
    print(f"""APROVADO!
Nota corte: 7 a 10
Sua média {media:.1f}.""")
