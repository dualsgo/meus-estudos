# MIMO - Operadores 'and' e 'or' com Tabela Verdade

# Às vezes, temos mais de uma condição e precisamos que todas sejam atendidas ou que pelo menos uma delas seja.

condicao1 = True
condicao2 = False

# Operador 'and' (e): Este operador nos permite executar um código somente se ambas as condições forem atendidas.
if condicao1 and condicao2:
    print('Se ambas as condições forem atendidas, este texto será exibido.')
# Neste exemplo, somente a condição 1 é True, portanto NÃO atende os requisitos dessa declaração condicional e o texto NÃO é exibido.

# Operador 'or' (ou): Este operador nos permite executar um código se pelo menos uma das condições for atendida.
if condicao1 or condicao2:
    print('Se pelo menos uma das condições for atendida, este texto será exibido.')
# Neste exemplo, somente a condição 1 é True, portanto atende os requisitos dessa declaração condicional e exibe o texto.

# Tabela Verdade do Operador 'and':
# | Condição 1 | Condição 2 | Resultado |
# |------------|------------|-----------|
# |    True    |    True    |   True    |
# |    True    |   False    |   False   |
# |   False    |    True    |   False   |
# |   False    |   False    |   False   |

# Tabela Verdade do Operador 'or':
# | Condição 1 | Condição 2 | Resultado |
# |------------|------------|-----------|
# |    True    |    True    |   True    |
# |    True    |   False    |   True    |
# |   False    |    True    |   True    |
# |   False    |   False    |   False   |
