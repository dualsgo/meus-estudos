# MIMO - 02 - Tipos e comparações

# 02.4 - Formatando strings

# Vamos aprender a exibir diferentes tipos de valores juntos no console com um recurso útil conhecido como strings formatadas.

# Aprendemos que podemos utilizar + para adicionar duas strings e exibi-las juntas.
print('Essa parte' + ' com essa.')

# Usar + para combinar dados numéricos com strings produz um erro.

# As f strings (abreviação de strings formatadas) nos permitem exibir expressões como adicionar um número a uma string, sem nenhum erro.

# Cada instrução f-string consiste em duas partes: primeiro o caractere f e depois a string que queremos, contendo um conjunto de chaves {} (abertura e fechamento) contendo o valor que desejamos exibir na instrução print().
print(f'{2} novas mensagens')

# Inserir variáveis entre as chaves também funciona.
nome = 'Ana'
print(f'Nome: {nome}')

# Também podemos usar expressões (com variáveis ou sem)
distancia = 10
distancia_percorrida = 4
print(f'Faltam percorrer {distancia - distancia_percorrida} Km.')

# Podemos usar quantas chaves forem necessárias.
print(f'A distância é de {distancia}Km. Você percorreu {distancia_percorrida}Km. Faltam percorrer {distancia - distancia_percorrida}Km.')

# Podemos armazenar a f-string em uma variável
notificacoes = 5
status = f'{notificacoes} novas notificações'
print(status)

