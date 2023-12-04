# MIMO - 08 - Funções
# 08.7.1 - Decidindo com funções

# Aninhando condicionais em funções

# E se quiséssemos que nossa função decida, como adicionar ou não o custo do frete, mas com base no fato do carrinho ter um determinado valor ou não?

# Para fazer uma condicional funcionar de maneira mais flexível, podemos usar o parâmetro da função, como carrinho, como parte da condição.
def add_carrinho(carrinho):
    # Usamos o recuo de dois espaços para aninhar a condicional dentro da função
    if carrinho < 100:
        # E outro recuo para aninhar o bloco de código da condicional
        return carrinho + 10
    else:
        return carrinho
# Ao codificar uma condicional dentro do bloco de código de uma função como add_carrinho, estamos aninhando dentro da função.

# Ao usar o parâmetro na condição, estamos usando o valor que passamos ao chamar a função, como 45 ou 200
print(add_carrinho(45))
print(add_carrinho(200))

# # 08.7.2 - Incorporando elif e outros

# Podemos aninhar todos os tipos de condicionais numa função, como esta instrução else. Também podemos aninhar instruções elif, como esta que verifica se o operador é igual a -

def calcular(operador, x, y):
    if operador == "+":
        return x + y
    elif operador == "-":
        return x - y
    else:
        print(f'Operador {operador} inválido.')
    print('Calculando...')
resultado = calcular('+', int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'O resultado é {resultado}')

# Mesmo que a condicional seja ignorada, o restante do bloco de código da função é executato