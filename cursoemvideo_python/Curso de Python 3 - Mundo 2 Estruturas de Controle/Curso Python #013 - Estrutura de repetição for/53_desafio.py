# Exercício Python #053 - Detector de Palíndromo - Aula 00 até 13
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite sua frase ou palavra: ')).strip().upper()  # Solicita e converte a frase para maiúsculas e remove espaços extras
# Remove espaços da frase original
frase = frase.split() # Separa a frase em palavras
nova_frase = []  # Inicializa a variável para armazenar a nova frase invertida

# Inverte a frase
for palavra in frase: # Percorre cada palavra da frase
    nova_palavra = '' # Inicializa a variável para armazenar a nova palavra invertida
    for letra in palavra[::-1]: # Percorre cada letra da palavra de trás para frente
        nova_palavra += letra  # Adiciona cada letra invertida à nova frase
    nova_frase.append(nova_palavra) # Adiciona cada palavra invertida à nova frase

print(f'A frase digitada foi: {' '.join(frase)}') # Imprime a frase original
print(f'O inverso da frase é: {' '.join(nova_frase)}') # Imprime a frase invertida

# Verifica se é um palíndromo
if nova_frase == frase:
    print('A frase é um palíndromo!') # Imprime se for um palíndromo
else: 
    print('A frase não é um palíndromo!') # Imprime se não for um palíndromo













"""# Tarefa 1: Ler a palavra ou frase
frase = str(input('Digite a palavra ou frase: ')).strip().upper()
frase_palavras = frase.split()
frase_sem_espaco = ''.join(frase_palavras)
frase_invertida = frase_sem_espaco[::-1]
print(f'A frase {frase_sem_espaco} ao contrário é {frase_invertida}')
palindromo = frase_sem_espaco == frase_invertida
if palindromo:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')"""