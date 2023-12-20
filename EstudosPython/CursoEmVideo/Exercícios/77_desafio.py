# Exercício Python #077 - Contando vogais em Tupla - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Tupla de palavras
palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Grátis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

# Loop principal: itera sobre cada palavra na tupla
for palavra in palavras:
    # Imprime a palavra e inicia a impressão das vogais
    print(f'A palavra "{palavra}" tem as vogais: ', end='')

    # Loop interno: itera sobre cada caractere na palavra
    for vogal in palavra:
        # Verifica se o caractere é uma vogal (considerando vogais com acentos)
        if vogal in 'AaÁáÀàEEÉéÈèIiÌìÍíOoÒÒÓóUuùÙÚú':
            # Imprime a vogal encontrada
            print(vogal, end=' ')

    # Pula para a próxima linha após imprimir as vogais da palavra atual
    print('')

