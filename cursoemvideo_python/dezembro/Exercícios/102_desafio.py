# Exercício Python #102 - Função para Fatorial - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(fatores, mostrar='S'):
    """
    Calcula o fatorial de um número
    :param fatores: número a ser calculado
    :param mostrar: exibe ou não o cálculo
    :return: retorna o resultado
    """
    fact = 1
    print(f'{fatores}! = ', end='')
    for fator in range(fatores, 0, -1):
        if mostrar == 'S':
            print(f'{fator} X ' if fator > 1 else f'{fator} = ', end='')
        fact *= fator
    return print(fact)


fatorial(int(input('Qual fatorial deseja ver? ')),
         str(input('Mostrar cálculo? S/N')).strip().upper())