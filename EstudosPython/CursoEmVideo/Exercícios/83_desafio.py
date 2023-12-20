# Exercício Python #083 - Validando expressões matemáticas - Aula 00 até 17 - Mundo 3
#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []

expressao = str(input('Digite a expressão: ')).strip()

for caractere in expressao:
    if caractere == '(':
        lista.append(caractere)
    elif caractere == ')':
        lista.append(caractere)
        if '(' in lista:
            lista.remove('(')
            lista.remove(')')


lista_vazia = len(lista)
print(len(lista))
print('\033[1;32mA expressão é válida!\033[m' if lista_vazia == 0 else '\033[1;31mExpressão inválida!\033[m')