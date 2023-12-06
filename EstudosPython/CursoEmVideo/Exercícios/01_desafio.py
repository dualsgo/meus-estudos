# Exercício Python #001 - Deixando tudo pronto - Aula 00 até 04
# Crie um programa que escreva 'Olá, mundo!' na tela.
from emoji import emojize
# Tarefa 1: Escrever a mensagem na tela

# Método 1
print('\033[1;32mMensagem direto no console com a função print():\033[m')
print(emojize('Olá, mundo! :globo_mostrando_as_américas:', language='pt'))

# Método 2
print('\n\033[1;32mMensagem no console utilizando a variável para exibir o valor:\033[m')
mensagem = emojize('Olá, mundo! :globo_mostrando_as_américas:', language='pt')
print(mensagem)

# Método 3
print('\n\033[1;32mMensagem no console utilizando o valor passado pelo usuário e atribuindo-o a uma variável:\033[m')
mensagem = input('Digite a mensagem: ')
print(mensagem)

