# Exercício Python #040 - Aquele clássico da Média
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# Tarefa 1: Receber as duas notas e calcular a média
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2
# Tarefa 2: Definir as condições e mensagens
print(f'Sua média foi: {media} - ', end='')
if media < 5:
    print('REPROVADO!')
elif media < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
# Tarefa 3: Mostrar o resultado
