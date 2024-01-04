# Exercício Python #108 - Formatando Moedas em Python - Aula 00 até 21 - Mundo 3
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from pacoteexercicios import moeda

valor = float(input('Digite um valor: '))

# Mostrando em formato monetário - R$ REAL BRL

print(f'Você possui {moeda.moeda(valor)} na carteira')