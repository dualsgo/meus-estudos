# Curso Python Aula 09 - Manipulando texto

"""RESUMO"""
# Introdução aos conceitos de manipulação de strings em Python e sua importância na programação.

# Explicação do armazenamento de strings em variáveis com uso de aspas.

# Demonstrações de slicing, que permite extrair partes específicas de uma string definindo índices de início e fim.

# Apresentação de técnicas de manipulação de texto, incluindo contagem de caracteres e localização de substrings.

# Demonstração de funções para substituir, converter para maiúsculas/minúsculas, e formatar strings.

# Explicação de como remover espaços em branco e dividir strings em elementos usando separadores.

# Demonstração de como unir elementos de uma lista de strings com um separador.

# Apresentação de funcionalidades para manipulação avançada de strings, como extrair letras específicas e contar caracteres.

# Introdução às limitações de mutabilidade de strings em Python e a necessidade de usar funções de transformação.

# Apresentação de desafios para os espectadores praticarem os conceitos aprendidos.

# Apresentação de um desafio adicional para criar um programa que realiza várias operações com strings.

# Incentivo aos espectadores para continuar aprendendo e explorar os exercícios adicionais do curso.
# Agradecimento aos contribuidores e encorajamento para que os estudantes compreendam os conceitos em vez de copiar cegamente código.
# Motivação para perseverar na aprendizagem e continuar estudando.
# Encerramento do vídeo com a promessa de mais conteúdo nas próximas aulas.

"""CONTEÚDO"""

# Cadeias de caracteres (strings): São sequências de texto envolvidas em aspas simples ou duplas e podem conter letras, números e caracteres especiais.
frase = 'Curso em Vídeo Python'

# Fatiamento
# Usamos a sintaxe variavel[inicio:fim:regra] para acessar partes da string.
# Por exemplo, para acessar o caractere 'V' no índice 9:
print(frase[9])  # Exibirá 'V'

# Para acessar o intervalo 'Víde' (do índice 9 até 12, excluindo o 13):
print(frase[9:13])  # Exibirá 'Víde'

# Podemos usar a regra para pular caracteres, por exemplo, pegar a cada 2 caracteres:
print(frase[9:21:2])  # Exibe 'VdoPo'

# Omitindo o início, começa do índice zero:
print(frase[:5])  # Exibe 'Curso' - Seria o mes

# Omitindo o fim, indica o início e vai até o final, independente do tamanho:
print(frase[15:])  # Exibe 'Python'

# Considera o início e pula a cada 3 caracteres até o final:
print(frase[9::3])  # Exibe 'VePh'

# Análise

# len(): Retorna o comprimento da string.
print(len(frase))

# .count(): Conta a quantidade de um caractere em uma cadeia.
print(frase.count('o'))  # Retorna o número de ocorrências de 'o'

# Podemos usar fatiamento para contar em um intervalo:
# variavel.count('string', incio, fim)
print(frase.count('o', 0, 13))  # Contagem de 'o' nos primeiros 13 caracteres
# Se omitir o intervalo irá considerar toda a string

# .find(): Exibe o índice de início da ocorrência de um conjunto de caracteres.
# Exibe o índice de início de 'deo' (ou -1 se não encontrado)
print(frase.find('deo'))

# Operador 'in': Verifica se um caractere ou conjunto de caracteres está na string.
print('Curso' in frase)  # Retorna True

# Transformação

# .replace(): Substitui um valor na string, criando uma nova string. A mudança só vale para aquela instância. Para mudar o valor pemantentemente deve-se atribuir o novo valor a variável ou a uma nova
# replace('string que deseja mudar', 'novo valor')
nova_frase = frase.replace('Python', 'Android')
print(frase, nova_frase, frase)

# .upper(): Transforma a string em maiúsculas.
print(frase.upper())

# .lower(): Transforma a string em minúsculas.
print(frase.lower())

# .capitalize(): Capitaliza apenas o primeiro caractere da string.
print(frase.capitalize())

# .title(): Capitaliza o primeiro caractere de cada palavra com base nos espaços.
print(frase.title())

# Removendo espaços extras no início e no fim:
frase_espacada = '   Aprenda Python   '

# .strip(): Remove espaços em branco no início e no fim.
print(frase_espacada.strip())

# Existem variações como rstrip() e lstrip() para remover espaços da direita e da esquerda, respectivamente.

# Divisão

# .split(): Divide a string usando espaços como separadores (por padrão, mas podemos definir outro separador entre os parênteses) e cria uma lista de palavras. Cada palavra é um elemento e receberá um índice
frase_split = frase.split()
print(frase_split)  # Exibirá ['Curso', 'em', 'Vídeo', 'Python']
# Podemos exibir o índice zero de frase_split
print(frase_split[0])  # Exibirá 'Curso'
# Além de mostrar um caracter em um índice específico
print(frase_split[0][3])  # Exibirá a letra s que está no indice indicado

# Junção

# '-'.join(frase_split): Reúne elementos da lista em uma string, usando '-' como separador.
frase_junta = '-'.join(frase_split)
print(frase_junta)  # Exibe 'Curso-em-Vídeo-Python'
# Podemos selecionar o separador, o colocando entre as aspas

# Três aspas exibem a string exatamente da forma que o código é digitado

print("""Portanto
  mesmo
        que
        
            hajam espaços
e linhas, serão mostrados da forma que foi digitado.""")
