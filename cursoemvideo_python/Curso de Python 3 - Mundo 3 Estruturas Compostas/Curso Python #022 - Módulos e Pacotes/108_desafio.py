# Exercício Python #108 - Formatando Moedas em Python - Aula 00 até 21 - Mundo 3
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from pacoteexercicios import moeda

valor = moeda.obter_valor_valido('Digite um valor: ')
print(f'Você possui {moeda.moeda(valor)} na carteira')