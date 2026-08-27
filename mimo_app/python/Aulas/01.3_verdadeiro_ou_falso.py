# MIMO - 01 - Noções básicas de Python

# 01.3 - Verdadeiro ou falso

# Há um valor especial que não é numa cadeia de caracteres nem um número: (True).
# Não há aspas em torno dele, e não é um valor numérico.

# True é ótimo para situações como verificar se um recurso está ativado ou se os dados estão disponíveis.

# Podemos armazenar em uma variável como uma cadeia de caracteres ou um número. Exibi-lo também funciona da mesma forma.
ligado = True  # Indica que algo está ligado
print(f'Está ligado? {ligado}')

# False é outro valor especial e o oposto de True.
# Podemos salvar False em uma variável.
ligado = False
print(f'Está ligado? {ligado}')

# "True" e "False" ou true e false não são o mesmo que True e False!

# Negando valores - Operador de negação not

# O código not na frente de True faz com que a expressão resulte em False. Se algo não é verdade, tem que ser falso. O not é o operador de negação que transforma os valores em seu oposto.

# Quando mudamos um valor para o seu oposto com not, nós o negamos. O operador not antes de False altera seu valor para True. Se um valor não é False, tem que ser True.
verdade = True
nao_mentira = not False  # Também será True
# Uma não mentira é igual à verdade

mentira = False
nao_verdade = not True  # Também será False

# Podemos usar o operador com variáveis para negar seus valores.

# Nessa lógica poderíamos atribuir a variável mentira o valor not verdade. O oposto não seria possível, pois a variável mentira não poderia ser referenciada antes de ser criada.
print(f'not nao_verdade: {not nao_verdade}') # O resultado será True

ligado = True
desligado = not ligado
print(desligado)  # Não ligado, é desligado