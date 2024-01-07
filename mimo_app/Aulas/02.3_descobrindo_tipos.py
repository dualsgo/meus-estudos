# MIMO - 02 - Tipos e comparações

# 02.3 - Descobrindo tipos

# Já vimos alguns tipos de dados, como números e strings. Em termos de programação, esses valores são chamados de tipos.

# Strings (str) - São caracteres entre aspas duplas ou simples.
# Inteiros (int) - Representam números sem decimais.
# Ponto flutuante (float) - São números com um ou mais dígitos após a vírgula decimal.
# Boolean (bool) - Representam os valores especiais True e False.

# Conversão de tipos
# As vezes precisamos converter um tipo de dado para outro. Por exemplo, se quisermos comparar um número inteiro com um número de ponto flutuante, precisamos convertê-los para o mesmo tipo de dados. Se não fizermos isso, o Python retornará um erro.
# Existem métodos integrados para nos ajudar a converter tipos de dados, mas antes precisamos saber se é possível converter um tipo de dado em outro.

# Vimos os tipos de dados básicos em Python. Se não tivermos certeza do tipo de valor, podemos verificá-lo. O método type() verifica o tipo de dado.
# Podemos verificar o tipo de qualquer variável com type(), colocando-a entre os parênteses.

# Se combinarmos o método type() com o método print(), podemos ver uma versão abreviada do tipo de dado no console
dado = 100  # A variável recebe um valor do tipo inteiro
print(type(dado))  # Exibe <class 'int'>

# Às vezes queremos alterar valores de um tipo para outro. Isso é chamado de conversão de tipo.
# Python possui alguns métodos integrados para nos ajudar a converter os tipos de dados. Por exemplo:

# A variável recebe um valor do tipo string
idade = '17'
# int() nos ajudará a converter o valor da string idade para um número inteiro, de modo que seja possível realizar a comparação sem causar um erro.
idade = int(idade)
# Agora podemos comparar a idade com o valor 18.
print(idade < 18)  

# O método str() nos permite pegar valores numéricos e convertê-los em strings.
ano = 2023
print(type(ano))
ano = str(ano)
# Agora podemos concatenar o ano com uma string.
print('O ano é ' + ano)
# Obs.: Não podemos concatenar um número com uma string. Isso causará um erro. Mas seria possível utilizar a vírgula para combinar os valores de diferentes tipos dentro do print().

# Se usarmos int() em números de ponto flutuante, simplesmente removeremos o ponto decimal e os valores subsequentes. Não haverá arredondamento!
preco = 9.99
print(int(preco))

# Obs.: Se quisermos arredondar um número de ponto flutuante, podemos usar round(). Isso arredondará o número para o inteiro mais próximo.
preco = round(preco)
print(preco) # 10

# Da mesma forma podemos utilizar float() em um número inteiro. Isso adicionará um ponto decimal e a capacidade de armazenar valores fracionários.
meses = 12
print(float(meses)) # 12.0


# Se utilizarmos int() em um boolean, o valor numérico equivalente será 1 para True e 0 para False (1.0 e 0.0 caso seja converta para float).
print(float(True))
print(int(False))

# Podemos usar bool() para converter uma variável para boolean. Se a variável tiver conteúdo ela se tornará True. Se estiver vazia ou for 0, ela se tornará False.

nome = 'Maycon'  # A variável recebe um valor do tipo string
print(bool(nome)) # True

sobrenome = ''  # A variável recebe um valor do tipo string vazio
print(bool(sobrenome)) # False

idade = 30  # A variável recebe um valor do tipo inteiro diferente de 0
print(bool(idade)) # True

dinheiro = 0  # A variável recebe um valor do tipo inteiro igual a 0
print(bool(dinheiro))  # False