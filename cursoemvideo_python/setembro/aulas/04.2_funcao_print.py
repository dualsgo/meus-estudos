# MIMO - Instrução print()

# Linhas de código são instruções que o computador deve seguir. A ordem é importante, pois o computador segue as instruções linha por linha.

# Com a instrução print(), dizemos ao computador para exibir um valor no console (também chamado de shell).
print('Esse texto será exibido quando o programa for executado!')

# Podemos usar essa instrução quantas vezes quisermos. Cada valor é exibido em uma nova linha.
print('Esse valor será exibido primeiro.')
print('Esse valor será exibido em seguida.')

# Podemos exibir variáveis. Nesse caso, o seu valor será exibido, não o nome.
variavel_exemplo = 'Esse é o valor da variável. Ele será exibido no console.'
print(variavel_exemplo)

# Podemos unir valores de string com o operador +. Chamamos isso de expressão, e a saída cria um valor único.
junto = 'Essa parte' + ' se junta a essa.'
print(junto)

# Quando as expressões têm variáveis, seus valores são unidos.
texto_1 = 'Essa parte'
texto_2 = ' se junta a essa.'
print(texto_1 + texto_2)

# As expressões são valores e, como tal, podem ser armazenadas em outra variável.
expressao = texto_1 + texto_2
print(expressao)

# DADOS NUMÉRICOS: São os dígitos numéricos. Eles não usam aspas.

# Podemos criar também expressões com números. As variáveis com dados numéricos podem ser usadas para cálculos.
valor_1 = 5
print(valor_1 + 3)  # Exibirá 8

# Podemos atribuir o resultado das expressões numéricas a uma variável.
res = valor_1 + 3
print(res)  # Exibirá 8

# Opções 'end' e 'sep' da instrução print()

# A instrução print() oferece duas opções adicionais: 'end' e 'sep'.

# A opção 'end' permite especificar o que deve ser impresso no final da saída. O valor padrão é '\n' (uma nova linha).
print('Este texto', end=' ')
print('será exibido na mesma linha.')

# A opção 'sep' permite especificar o separador entre os valores a serem impressos. O valor padrão é um espaço.
horas = 10
minutos = 20
print(horas, minutos)  # Exibirá "10 20"
print(horas, minutos, sep=':')  # Exibirá "10:20"
