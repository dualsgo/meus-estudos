# MIMO - Convertendo Tipos de Dados

# Às ,vezes podemos querer converter valores de um tipo para outro. Para isso, utilizamos algumas funções integradas.

# int(): Converte para números inteiros.
# Se usarmos int() em um float, o ponto decimal e o valor subsequente são removidos.
print(int(2.9))  # Exibe 2

# Se usarmos int() em um booleano, o valor equivalente para True é 1, e para False, é 0.
print(int(True))
print(int(False))

# float(): Converte para números de ponto flutuante.
# Se usarmos float() em um inteiro, um ponto decimal é adicionado.
print(float(10))  # Exibe 10.0
print(float(True))
print(float(False))

# str(): Converte para strings.
# Se usarmos str() em um booleano, exibirá a palavra/texto equivalente, assim como valores numéricos.
print('True', end=' === ')
print(type('True'))
print(str(True), end=' === ')
print(type(str(True)))

# bool(): Converte para booleanos.
# Podemos usar bool() para converter uma variável em booleano. Se ela possuir conteúdo, o valor equivalente é True.
variavel = "Exibirá True"
print(bool(variavel))
print(bool(1))

# Se ela estiver vazia, o valor equivalente é False.
variavel = ""
print(bool(variavel))
print(bool(0))
