# Exercício Python #026 - Primeira e última ocorrência de uma string - Aulas 00 até 09 - Mundo 1
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

from unidecode import unidecode # pip install unidecode
# remove acentos e caracteres especiais

# Tarefa 1: Ler uma frase pelo teclado
frase = str(input('Digite uma frase qualquer: ')).strip().upper()

# Tarefa 2: Mostrar as informações
# Ocorrências da letra A
ocorrencias_a = frase.count('A')
print(f'A letra "A" aparece {ocorrencias_a} vezes na frase.')

# Primeira ocorrência da letra A
primeira_ocorrencia = frase.find('A')
print(f'A letra "A" aparece pela primeira vez na posição {primeira_ocorrencia + 1}.')

# Última ocorrência
ultima_ocorrencia = frase.rfind('A')
print(f'A última aparição da letra "A" é na posição {ultima_ocorrencia + 1}')

# Versão 2 - Com unicode

frase = unidecode(input('Digite uma frase para analisarmos: ').strip().title())

# Laço para colorir a letra "a" na frase
for letra in frase:
    print(f'\033[31m{letra}\033[m' if letra in 'aA' else letra, end='')

print(f'\n{'Quantidade de "a":':<30}{frase.lower().count("a"):>2}')
print(f'{'A primeira posição de "a":':<30}{frase.lower().find("a")+1:>2}')
print(f'{'A última posição de "a":':<30}{frase.lower().rfind("a")+1:>2}')