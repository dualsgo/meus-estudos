# MIMO - Formatando strings

# Vimos antes que podemos concatenar strings utilizando o sinal de +. Dessa forma os valores são unidos e formam um só.
texto1 = 'Essa parte'
texto2 = ' se junta a essa.'
print(texto1 + texto2)  # Saída: 'Essa parte se junta a essa'

# O recurso de formatação de string (f string) nos possibilita formatar uma string de modo mais amplo

# A sintaxe é:# MIMO - Formatando Strings com F-strings e Caracteres de Escape

# Antes, vimos que podemos concatenar strings usando o sinal de +. Dessa forma, os valores são unidos e formam uma única string.
texto1 = 'Essa parte'
texto2 = ' se junta a essa.'
print(texto1 + texto2)  # Saída: 'Essa parte se junta a essa'

# O recurso de formatação de string (f-string) nos possibilita formatar uma string de modo mais amplo.

# A sintaxe é:
# f"Texto da string"
# f"Texto da string {expressões} ou {variáveis} entre as chaves"

# Exemplo de uso de f-strings para unir os valores das variáveis:
resultado = f'Dessa forma podemos unir o valor "texto1" com o valor "texto2" assim: {texto1}{texto2}'
print(resultado)

# Caracteres de Escape:
# Podemos usar caracteres de escape para inserir caracteres especiais em strings.
# Exemplos:
# - \n: Quebra de linha
# - \t: Tabulação (espaço de tabulação)
# - \': Aspas simples
# - \": Aspas duplas
# - \\: Barra invertida

# Exemplo com quebra de linha:
mensagem = "Primeira linha\nSegunda linha"
print(mensagem)

# Exemplo com tabulação:
codigo = "def funcao():\n\tprint('Olá, mundo!')"
print(codigo)

# Adicionando Cores com Códigos ANSI:
# Podemos adicionar cores ao texto no terminal usando códigos ANSI.
# A sintaxe geral é: \033[estilo;texto;fundo;codigodemarcaçãom;textopadrao
# Estilos: 0 (normal), 1 (negrito), 2 (fraco), 3 (itálico), 4 (sublinhado), 7 (inverter cores)
# Cores de Texto: 30 (preto), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul), 35 (magenta), 36 (ciano), 37 (branco)
# Cores de Fundo: 40 (preto), 41 (vermelho), 42 (verde), 43 (amarelo), 44 (azul), 45 (magenta), 46 (ciano), 47 (branco)

# Exemplo de texto vermelho em fundo amarelo:
mensagem_colorida = "\033[1;31;43mTexto vermelho em fundo amarelo\033[m"
print(mensagem_colorida)

# f"Texto da string"
# f"Texto da string {expressões} ou {variaveis} entre as chaves"

print(
    f'Dessa forma podemos unir o valor "texto1" com o valor "texto2" assim: {texto1}{texto2}')
