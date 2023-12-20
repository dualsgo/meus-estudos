"""Desafio 083 - Validando expressões matemáticas (Aula 01 a 17): Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

# Solicita ao usuário que digite uma expressão
expressao = input('Digite a expressão: ')

# Inicializa uma lista para rastrear os parênteses
lista = []

# Percorre cada caractere na expressão
for letra in expressao:
    # Se encontrar '(', adiciona à lista
    if letra == '(':
        lista.append(letra)
    # Se encontrar ')'
    elif letra == ')':
        # Verifica se há '(' na lista
        if '(' in lista:
            # Remove o '(' correspondente
            lista.remove('(')
        else:
            # Se não houver '(', adiciona ')' à lista
            lista.append(letra)

# Verifica se a lista está vazia, indicando parênteses balanceados
if len(lista) < 1:
    print('Expressão válida!')
else:
    print('Expressão inválida!')

################# Guanabara

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
