# Exercício Python #053 - Detector de Palíndromo - Aula 00 até 13
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite sua frase ou palavra: ')).strip().upper()  # Solicita e converte a frase para maiúsculas e remove espaços extras
nova_frase = ''  # Inicializa a variável para armazenar a nova frase invertida

# Remove espaços da frase original
frase = frase.split()  # Divide a frase em uma lista de palavras
frase = ''.join(frase)  # Junta as palavras para formar a frase sem espaços

# Inverte a frase
for letra in frase[::-1]:
    nova_frase += letra  # Adiciona cada letra invertida à nova frase

print(f'A frase digitada foi: "{frase}"')  # Exibe a frase original sem espaços
print(f'O inverso da frase é: "{nova_frase}"')  # Exibe a nova frase invertida sem espaços

# Verifica se é um palíndromo
if nova_frase == frase:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')













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

