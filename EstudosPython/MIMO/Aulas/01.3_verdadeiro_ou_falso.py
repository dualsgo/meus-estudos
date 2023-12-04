# MIMO - 01 - Noções básicas de Python

# 01.3 - Verdadeiro ou falso

"""
Há um valor especial que não é numa cadeia de caracteres nem um número: (True). Não há aspas em torno dele, e não é um valor numérico.
"""

# True é ótimo para situações como verificar se um recurso está ativado ou se os dados estão disponíveis. 

# Podemos armazenar em uma variável como uma cadeia de caracteres ou um número. Exibi-lo também funciona da mesma forma.
ligado = True
print(ligado)

"""
False é outro valor especial e o oposto de True.
"""

ligado = False
print(ligado)

# Negando valores - Operador de negação not

# O código not na frente de True faz com que a expressão resulte em False. Se algo não é verdadeiro, tem que ser falso. not é o operador de negação. Transforma os valores em seu oposto.

# Quando mudamos um valor para o seu oposto com not, nós o negamos. O operador not antes de False altera seu valor para True. Se um valor não é False, tem que ser True.
verdade = True
mentira = False

nao_verdade = not True
# Uma não verdade é o mesmo que uma mentira

nao_mentira = not False
# Uma não mentira é igual à verdade

# Podemos usar o operador com variáveis para negar seus valores. 

ligado = True
print(not ligado) # Não ligado, é desligado

