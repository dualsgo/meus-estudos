# Exercício Python #040 - Aquele clássico da Média - Aula 00 até 12 - Mundo 2
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# Tarefa 1: Receber as duas notas e calcular a média
primeira_nota = float(input('Digite a primeira nota: '))
print(f'Nota do primeiro bimestre: {primeira_nota:.1f}')
segunda_nota = float(input('Digite a segunda nota: '))
print(f'Nota do segundo bimestre: {segunda_nota:.1f}')

media = (primeira_nota + segunda_nota) / 2
# Tarefa 2: Definir as condições e mensagens
print(f'\033[1mSua média foi: {media:.1f} - \033[m', end='')
if media < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif media < 7:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')
# Tarefa 3: Mostrar o resultado
