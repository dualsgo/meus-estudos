""" Desafio 001 - Deixando tudo pronto (Aula 01 a 04): Crie um programa que escreva "Olá, Mundo!" na tela."""

# Podemos exibir a mensagem diretamente no console ou guardá-la em uma variável

# Primeiro método
mensagem = '\033[1;31mOlá, mundo!\033[m'
print(mensagem)
# Segundo método
print("\033[1;32mOlá, Mundo!\033[m")
