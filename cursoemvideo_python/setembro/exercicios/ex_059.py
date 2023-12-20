"""Desafio 059 -  Criando um Menu de Opções (Aula 01 a 14): Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
O programa deve realizar a operação solicitada em cada caso
"""
from time import sleep
print(""""
FAÇA SUA ESCOLHA
""")
sleep(1)
# Ler os dois valores
valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
# Inicialize a opção com zero para entrar no loop
opcao = 0
# Laço de repetição, enquanto a opção selecionada não for a 5
while opcao != 5:
    opcao = int(input(""">>>>>>>>>>>>>>>>>>>>>>>>>
\033[1;32mSELECIONE A OPÇÃO\033[m
[1] Somar os valores
[2] Multiplicar os valores
[3] Verificar o maior valor
[4] Digitar novos valores
[5] Encerrar o programa
>>>>>>>>>>>>>>>>>>>>>>>>>
Qual é a sua escolha? """))
# OPÇÃO 1 SOMAR
    if opcao == 1:
        sleep(1)
        print('\033[1;32mSOMAR\033[m')
        print(f'A soma entre \033[1;32m{valor_1}\033[m e \033[1;32m{valor_2}\033[m é \033[1;32m{valor_1 + valor_2}\033[m.')
# OPÇÃO 2 MULTIPLICAR
    elif opcao == 2:
        sleep(1)
        print('\033[1;32mMULTIPLICAR\033[m')
        print(f'O produto dos fatores \033[1;32m{valor_1}\033[m e \033[1;32m{valor_2}\033[m é \033[1;32m{valor_1 * valor_2}\033[m')
# OPÇÃO 3 VERIFICAR O MAIOR
    elif opcao == 3:
        sleep(1)
        print('\033[1;32mMAIOR\033[m')
        if valor_1 > valor_2:
            print(f'Entre os valores \033[1;32m{valor_1}\033[m e \033[1;32m{valor_2}\033[m, o valor \033[1;32m{valor_1}\033[m é o maior!')
        else:
            print(f'Entre os valores \033[1;32m{valor_1}\033[m e \033[1;32m{valor_2}\033[m, o valor \033[1;32m{valor_2}\033[m é o maior!')
# OPÇÃO 4 DIGITAR NOVOS NUMEROS
    elif opcao == 4:
        sleep(1)
        print('\033[1;32mNOVOS VALORES\033[m')
        valor_1 = int(input('Digite um novo valor: '))
        valor_2 = int(input('Digite um novo valor: '))
# OPÇÃO MAIOR QUE 5 OPÇÃO É INVÁLIDA
    elif opcao > 5:
        sleep(1)
        print('\033[7;31;40mOPÇÃO INVÁLIDA!\033[m')
    sleep(1)
# OPÇÃO 5 SAI DO PROGRAMA
print('\033[7;31;40mPROGRAMA FINALIZADO!\033[m')
