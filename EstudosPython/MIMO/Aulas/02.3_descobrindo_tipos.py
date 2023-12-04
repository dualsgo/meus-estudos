# MIMO - 02 - Tipos e comparações

# 02.3 - Descobrindo tipos

# Já vimos alguns tipos de dados, como números e strings. Em termos de programação, esses valores são chamados de tipos.

# Strings (str) - São caracteres entre aspas duplas ou simples.
# Inteiros (int) - Representam números sem decimais.
# Ponto flutuante (float) - São números com um ou mais dígitos após a vírgula decimal.
# Boolean (bool) - Representam os valores especiais True e False.

# Conversão de tipos

# Vimos os tipos de dados básicos em Python. Se não tivermos certeza do tipo de valor, podemos verificá-lo. O método type() verifica o tipo de dado.
# Podemos verificar o tipo de qualquer variável com type(), colocando-a entre os parênteses.

# Se combinarmos o método type() com o método print(), podemos ver uma versão abreviada do tipo de dado no console
dado = 2023
print(type(dado)) # Exibe <class 'int'>

# Às vezes queremos alterar valores de um tipo para outro. Isso é chamado de conversão de tipo.
# Python possui alguns métodos integrados para nos ajudar a converter os tipos de dados. Por exemplo:

# A variável recebe um valor do tipo string
idade = '17'

# int() nos ajudará a converter o valor da string idade para um número inteiro, de modo que seja possível realizar a comparação sem causar um erro.
print(int(idade) < 18)

# O método str() nos permite pegar valores numéricos e convertê-los em strings.
ano = 2023
print(str(ano))

# Se usarmos int() em números de ponto flutuante, simplesmente removeremos o ponto decimal e os valores subsequentes. Não haverá arredondamento!
preco = 9.99
print(int(preco))

# Da mesma forma podemos utilizar float() em um número inteiro. Isso adicionará um ponto decimal e a capacidade de armazenar valores fracionários.
meses = 12
print(float(meses))

# Se utilizarmos int() em um boolean, o valor numérico equivalente será 1 para True e 0 para False (1.0 e 0.0 caso seja converta para float).
print(int(True))
print(int(False))

# Podemos usar bool() para converter uma variável para boolean. Se a variável tiver conteúdo ela se tornará True. Se estiver vazia ou for 0, ela se tornará False.

nome = 'Maycon'
print(bool(nome))
sobrenome = ''
print(bool(sobrenome))
idade = 30
print(bool(idade))
dinheiro = 0
print(bool(dinheiro))

