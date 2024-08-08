# Exercício Python #083 - Validando expressões matemáticas - Aula 00 até 17 - Mundo 3
#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

def processar_parenteses(expressao):
    parenteses = []
    for caractere in expressao:
        if caractere == '(':
            parenteses.append('(')
        elif caractere == ')':
            if '(' in parenteses:
                parenteses.remove('(')
    return parenteses


parenteses = processar_parenteses(input('Digite a expressão: ').strip())

print(f'A expressão {'\033[1;31mNÃO\033[m' if parenteses else '\033[1;32mÉ\033[m'} válida!')