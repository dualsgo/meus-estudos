"""Desafio 034 - Aumentos multiplos (Aula 01 a 10): Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

- Para salários superiores a R$ 1250,00 calcule um aumento de 10%.
- Para os inferiores ou iguais, o aumento é de 15%."""
print("""
      \033[1;45mAUMENTO SALARIAL\033[m""")
# Passo 1: Peguntar o salário - Atribuimos a uma variável o valor que será digitado através de um método input e convertido pra float
print('Digite o seu salário: \n')
salario = float(input(''))
# Passo 2: Calcular o valor do aumento -

# Verificar a faixa salarial
if salario >= 1250:  # Se for maior ou igual a 1250
    print(f"""\033[1mSeu salário base é R$ {salario:.2f}\033[m
\033[1;44mSEU AUMENTO SERÁ DE 10%.\033[m""")
    salario = salario + (salario * .1)
    print(
        f'\033[1mSeu novo salário passa a ser R$ {salario:.2f}\033[m.')
else:  # Se for menor
    print(f"""\033[1;mSeu salário base é R$ {salario:.2f}\033[m
\033[1;45mSEU AUMENTO SERÁ DE 15%.\033[m""")
    salario = salario + (salario * .15)
    print(
        f'\033[1mSeu novo salário passa a ser R${salario:.2f}.\033[m')
