# Exercício Python #083 - Validando expressões matemáticas
# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


expressão = input('Digite a expressão: ').strip()
parênteses = []

for parêntese in expressão:
    if parêntese == '(':
        parênteses.append(parêntese)

    elif parêntese == ')':
        parênteses.append(parêntese)

        if '(' in parêntese:
            parênteses.remove('(')
            parênteses.remove(')')

print('Expressão', 'INVÁLIDA' if len(parênteses) else 'VÁLIDA')