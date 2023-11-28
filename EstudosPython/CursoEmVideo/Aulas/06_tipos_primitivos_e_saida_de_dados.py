# Curso Python #06 - Tipos Primitivos e Saída de Dados

# A função input() retorna um valor do tipo string por padrão, mesmo que um número seja digitado.
print('Saída do input() padrão sem conversão:')
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

# Devido a isso o sinal + não irá somar os valores e sim concatenar (unir).
soma = n1 + n2
print('A soma entre', n1, 'e', n2, 'é igual a', soma)

# A funçã o type() é útil para verificar os tipos de dados dos valores. A sintaxe é type(valor) - pode ser uma variável.
print(type(n1))
print(type(n2))
print(type(soma))
print('Saída do input() convertido:')
# Existem funções que convertem os valores para tipos de dados diferentes. Nesse exemplo usamos int() para converter o input() de string - str para integer - int.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma entre', n1, 'e', n2, 'é igual a', soma)

# Podemos exibir valores de variáveis em um print() usando uma formatação especial. Em vez de concatenar com vírgula, usamos uma máscara {} e um método .format() para substituir a máscara por um valor

print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))

# A outra forma e mais recente são as f-strings. Utilizamos um f antes da string para indicar que é uma f-string e colocamos o valor dento das chaves.

print(f'A soma entre {n1} e {n2} é igual a {soma}.')

print('\n============ Parte prática ============\n')
# Os resultados são os mesmos!
print('Saída do console da função type():')
# Os principais tipos primitivos são:
inteiros = 2 # int - Números inteiros
print(type(inteiros))
ponto_flutuante = 2.0 # float - Números com casas decimais após a vírgula
print(type(ponto_flutuante))
boolean = True # bool - Valores lógicos, True ou False
print(type(boolean))
strings = 'Caracteres entre aspas' # str - Cadeias de caracteres
print(type(strings))

# Se convertermos qualquer valor para str, o valor será exibido entre aspas
print(str(True))
# Se convertermos um valor inteiro para float, um ponto seguido de um zero serão adicionados ao número
print(float(1))
# Se convertermos um valor float para int, o ponto e as casas decimais serão removidas
print(int(3.1415))
# Ao converter uma string para bool, será exibido True. Se a string estiver vazia '' o valor é False
print(bool(''))
# Ao converter um número int ou float para bool, zero será equivalente a False e 1 (ou mais) será True
print(bool(0))
print(bool(1.0))
print(bool(42))
('Analisando dados:')
# Existem métodos para analisar as strings
algo = input('Digite algo: ')

print(algo.isnumeric()) # Verifica se o valor é um número para dizer se é possível converter para int ou float
print(algo.isalpha()) # Verifica se o valor é alfabético
print(algo.isalnum()) # Verifica se o valor possui letras e números
