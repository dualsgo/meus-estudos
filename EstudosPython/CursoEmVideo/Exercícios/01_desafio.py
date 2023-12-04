# Exercício Python #001 - Deixando tudo pronto - Aula 00 até 04
# Crie um programa que escreva 'Olá, mundo!' na tela.
from emoji import emojize
# Tarefa 1: Escrever a mensagem na tela
print('Mensagem direto no console com a função print():')
print(emojize('Olá, mundo! :globo_mostrando_as_américas:', language='pt'))
print('Mensagem no console utilizando a variável para exibir o valor:')
mensagem = emojize('Olá, mundo! :globo_mostrando_as_américas:', language='pt')
print(mensagem)
print('Mensagem no console utilizando o valor passado pelo usuário e atribuindo-o a uma variável:')
mensagem = input('Digite a mensagem: ')
print(mensagem)

