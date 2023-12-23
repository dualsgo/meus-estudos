# Exercício Python #083 - Validando expressões matemáticas - Aula 00 até 17 - Mundo 3
#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Inicializa uma lista vazia
lista = []

# Solicita ao usuário que digite a expressão
expressao = str(input('Digite a expressão: ')).strip()

# Itera sobre cada caractere na expressão
for caractere in expressao:
    # Se o caractere for '(', adiciona à lista
    if caractere == '(':
        lista.append(caractere)
    # Se o caractere for ')', verifica e remove o par correspondente '('
    elif caractere == ')':
        lista.append(caractere)
        # Verifica se existe um '(' na lista
        if '(' in lista:
            # Remove o '(' e o ')'
            lista.remove('(')
            lista.remove(')')

# Obtém o comprimento da lista após o processamento
lista_vazia = len(lista)

# Imprime se a expressão é válida ou inválida
print('\033[1;32mA expressão é válida!\033[m' if lista_vazia == 0 else '\033[1;31mExpressão inválida!\033[m')
