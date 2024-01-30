# MIMO - 02 - Tipos e comparações

# 02.4 - Formatando strings

# Vamos aprender a exibir diferentes tipos de valores juntos no console com um recurso útil conhecido como strings formatadas.

# Aprendemos que podemos utilizar + para adicionar duas strings e exibi-las juntas.
print('Essa parte' + ' com essa.')  

# Usar + para combinar dados numéricos com strings produz um erro.

# A solução seria utilizar vírgula (,) para concatenar valores diferentes em uma expressão.
print('Eu tenho', 30, 'anos')  # O separador padrão da vírgula é um espaço.
print('Podemos', 'mudar o separador', 'com sep', sep='****') # O separador pode ser alterado com o argumento sep.

# O RECURSO MAIS MODERNO:
# As f strings (abreviação de strings formatadas) nos permitem exibir expressões como adicionar um número a uma string, sem nenhum erro.

# Cada instrução f-string consiste em duas partes: primeiro o caractere f e depois a string que queremos, contendo um conjunto de chaves {} (abertura e fechamento) contendo o valor que desejamos exibir na instrução print().
print(f'{2} novas mensagens')

# Inserir variáveis entre as chaves também funciona.
nome = 'Ana'
print(f'Nome: {nome}')