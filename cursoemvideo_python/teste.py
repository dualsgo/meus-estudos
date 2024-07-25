# Criar um programa que receba uma quantidade que representará a quantidade de caracteres de uma senha. Mínimo 8 e máximo 16. O programa deverá gerar uma senha aleatória com a quantidade de caracteres informada.

# Para isso, serão sorteados 8 números aleatórios entre 33 e 126, que representam os caracteres da tabela ASCII.
# Os caracteres são: !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

# Os 8 números sorteados serão gerados a partir de um número binário de 8 bits. Para chegar a este número, sortearemos 8 números aleatórios entre 0 e 1.

# Converteremos esse número binário para decimal e, em seguida, para um caractere da tabela ASCII que será exibido na tela.
from random import randint

# Solicita ao usuário a quantidade de caracteres para a senha aleatória
quantidade_caracteres = int(input('Digite a quantidade de caracteres para sua senha aleatória: Min. 8 Max. 16 '))

# Inicializa uma lista vazia para armazenar os caracteres gerados
lista_caracteres = list()

# Loop para gerar a quantidade desejada de caracteres
for caractere in range(quantidade_caracteres):

    # Inicializa uma lista vazia para armazenar os dígitos binários
    lista_bin = list()

    # Loop para gerar 8 dígitos binários
    while len(lista_bin) < 8:
        # Gera dígitos binários aleatórios (0 ou 1)
        num_bin_sorteado = randint(0, 1)
        lista_bin.append(str(num_bin_sorteado))

    # Converte a lista de dígitos binários para uma string
    lista_editada = ''.join(lista_bin)

    # Converte a string binária para um número inteiro
    numero_valido = int(lista_editada, 2)

    # Verifica se o número está na faixa desejada (48 a 57, 65 a 90, 97 a 122)
    while not ((48 <= numero_valido <= 57) or (65 <= numero_valido <= 90) or (97 <= numero_valido <= 122)):
        # Se o número não estiver na faixa desejada, reinicia o loop
        lista_bin = []
        while len(lista_bin) < 8:
            num_bin_sorteado = randint(0, 1)
            lista_bin.append(str(num_bin_sorteado))

        lista_editada = ''.join(lista_bin)
        numero_valido = int(lista_editada, 2)

    # Converte o número para o caractere correspondente e adiciona à lista
    lista_caracteres.append(chr(numero_valido))

# Imprime a senha gerada na tela
for i in lista_caracteres:
    print(i, end='')

