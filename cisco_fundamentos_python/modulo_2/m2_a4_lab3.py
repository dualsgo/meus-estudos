# 2.4.10 LAB Operadores e Expressões
# Cenário
# Dê uma olhada no código no editor: ele lê um valor float, coloca-o em uma variável chamada x e imprime o valor de uma variável chamada y. Sua tarefa é completar o código para avaliar a seguinte expressão:

# 3x3 - 2x2 + 3x - 1
# O resultado deve ser atribuído a y.

# Lembre-se de que a notação algébrica clássica gosta de omitir o operador de multiplicação - você precisa usá-la explicitamente. Observe como mudamos o tipo de dados para garantir que x seja do tipo float.

# Mantenha seu código limpo e legível e teste-o usando os dados que fornecemos, atribuindo-o sempre à variável x (codificando-o). Não desanime por qualquer falha inicial. Seja persistente e inquisitivo.

"""# exemplo de entrada
x = 0
x = 1
x = -1
# Exemplo de saída
y = -1.0
y = 3.0
y = -9.0"""
x = 1
# 3x3 - 2x2 + 3x - 1
y = 3 * x * 3 - 2 * x * 2 + 3 * x - 1
print(y)