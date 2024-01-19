# Exercício Python #067 - Tabuada v3.0 - Aula 00 até 15 - Mundo 2
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

from emoji import emojize
from time import sleep
while True:
    numero = int(input('Qual número deseja ver a tabuada? '))

    # Verifica se o número é negativo para encerrar o programa
    if numero < 0:
        print(emojize('Encerrando o programa...', language='pt'))
        break

    # Loop para multiplicar o número pelos números de 1 a 10
    for contador in range(1, 11):
        multiplo = numero * contador
        # Exibe a tabuada usando emojis
        print(emojize(f'\033[1m{numero} :sinal_de_multiplicação: :tecla_{contador}: :sinal_de_igual: {multiplo:2}', language='pt'))
        sleep(0.5)



