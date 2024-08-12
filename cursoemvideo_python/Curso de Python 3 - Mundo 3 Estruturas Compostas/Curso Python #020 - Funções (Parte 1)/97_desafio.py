# Exercício Python #097 - Um print especial - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def exibe_texto_adaptado(texto):
    tamanho_texto = len(texto) + 10
    print(f'{'~' * tamanho_texto}')
    print(f'{texto.center(tamanho_texto)}')
    print(f'{'~' * tamanho_texto}')


exibe_texto_adaptado(input('Digite um texto e veja o resultado: ').strip())