""" Desafio 001 - Deixando tudo pronto (Aula 01 a 04): Crie um programa que escreva "Olá, Mundo!" na tela."""

# Podemos exibir a mensagem diretamente no console ou guardá-la em uma variável

# Primeiro método - Atribuindo a mensagem a uma variável
mensagem = '\033[1;31mOlá, mundo!\033[m'
# Depois exibindo, utilizando a variável na instrução print
print(mensagem)

# Segundo método - Exibindindo a mensagem diretamente na instrução print
print("\033[1;32mOlá, Mundo!\033[m")
