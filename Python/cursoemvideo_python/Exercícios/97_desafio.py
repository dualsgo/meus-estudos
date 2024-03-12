# Exercício Python #097 - Um print especial - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def escreva(texto_qualquer):
    tamanho = len(texto_qualquer) + 2
    print('~' * tamanho)
    print(f'{texto_qualquer:^{tamanho}}')
    print('~' * tamanho)


escreva(str(input('Digite o texto que deseja exibir: ')))