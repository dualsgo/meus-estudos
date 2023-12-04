# Exercício Python #002 - Respondendo ao Usuário - Aula 00 até 04
# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas conforme o valor digitado.

# Tarefa 1: Ler o nome de uma pessoa
nome = input('Digite o seu nome: ').strip()

# Tarefa 2: Mostrar uma mensagem de boas-vindas com o valor digitado.
print('Seja bem-vindo, ', nome, '! ', 'Prazer em te conhecer!', sep='')

# Saída formatada com .format()
print('É um prazer te conhecer, {}!'.format(nome))

# Saída formatada com f-string
print(f'É um prazer te conhecer, {nome}!')

# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

# Tarefa 1: Ler as informações - dia, mês e ano
dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')

# Tarefa 2: Mostrar a mensagem com a data formatada.
print('Você nasceu no dia ', dia, ' do mês de ', mes, ' do ano de ', ano, '. Correto?', sep='')
