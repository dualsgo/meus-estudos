# Curso Python Aula 11 - Cores no terminal

"""RESUMO"""
# Introdução ao tópico de trabalhar com cores no terminal usando Python.

# Explicação de que existem diferentes maneiras de alcançar isso, mas o foco será nas sequências de escape ANSI.

# Demonstração do uso do código de sequência de escape ANSI "\033[0;33m" para representar a cor amarela em Python.

# Mencionar que existem códigos para diferentes cores, mas o vídeo se concentrará apenas em alguns básicos.

# Ênfase na importância de continuar os estudos de programação e não desistir do curso.

# Explicação de como usar cores no terminal com Python.

# Exemplos de diferentes códigos para estilos, cores de texto e cores de fundo.

# Listagem dos códigos disponíveis para diferentes estilos e cores.

# Mencionar que a cor padrão do terminal é preta, mas pode ser personalizada.

# Demonstração de como aplicar cores ao texto no terminal usando os códigos fornecidos.

# Demonstração de como usar cores no terminal com Python.

# Mostrar diferentes códigos de cores para texto e cores de fundo, como vermelho, verde, branco e preto.

# Explicação de como criar diferentes estilos, como sublinhado e negrito.

# Fornecer exemplos e incentivar a experimentação com cores para criar efeitos personalizados.

# Mencionar que todos os códigos de cores podem ser encontrados na transcrição para referência.

# Demonstração de como adicionar cores ao terminal usando Python.

# Exemplos de alteração da cor de fundo, cor da fonte e destaque de texto.

# Mencionar que existem outras maneiras de trabalhar com cores no terminal, como o uso de valores hexadecimais.

# Introdução a um método mais avançado usando a função print para formatar texto com cores.

# Apresentação de diferentes maneiras de adicionar cores à saída do terminal em Python.

# Demonstração de como usar caracteres de escape e códigos especiais para alterar a cor do texto.

# Introdução a uma técnica usando um dicionário para definir uma lista de cores que podem ser usadas em todo o programa.

# Mencionar que existem várias abordagens para adicionar cores e sugerir escolher a que melhor se adequa à situação específica.

# Apresentação de um desafio aos espectadores para praticarem a adição de cores aos seus próprios programas.

# Encorajamento aos espectadores para praticarem e repetirem os exercícios ensinados na lição anterior sobre cores no terminal.

# Explicação de como a aplicação de cores aos programas pode torná-los visualmente mais atraentes e aumentar o conhecimento do usuário.

# Mencionar que os espectadores que concluíram os exercícios agora podem fazer uma avaliação e receber um certificado com uma pontuação mínima de 70%.

# Ênfase na importância de levar a avaliação a sério e não tentar fazê-la várias vezes, pois há um número limitado de tentativas permitidas.

# Expressão de dedicação à criação do melhor curso de Python e incentivo aos espectadores a compartilharem seu conhecimento com os outros.

# Sugestão de que, para trabalhar em projetos de programação mais avançados, é necessário aprender os conceitos básicos primeiro.

# Ênfase na importância de seguir o canal para conteúdo online e agradecimento aos espectadores pelo apoio.

# Menção de que a próxima seção do curso Python se concentrará em estruturas de controle.

"""CONTEÚDO"""
# ANSI - escape sequence

# Cores em Python \033[m

# O código vai entre [m
# \033[estilo;texto;fundom

# Estilos: 0 - Nenhum, 1 - Negrito, 4 - Sublinhado, 7 - Invertido (cor e background)
# Cores: 31 - Vermelho, 32 - Verde, 33 - Amarelo, 34 - Azul, 35 - Roxo, 36 - Azul claro, 37 - Cinza
# Background: 41 - Vermelho, 42 - Verde, 43 - Amarelo, 44 - Azul, 45 - Roxo, 46 - Azul claro, 47 - Cinza

# Exemplos de formatação
print('''
\033[41mTESTE\033[m - Fundo vermelho
\033[4;33;44mTESTE\033[m - Sublinhado, texto amarelo, fundo azul
\033[1;35;43mTESTE\033[m - Negrito, texto roxo, fundo amarelo
\033[42mTESTE\033[m - Fundo verde
\033[7;30mTESTE\033[m - Invertido, texto branco, fundo preto
\033[7mTESTE\033[m - Invertido, texto padrão, fundo padrão
''')

# Declaração, dicionário 'cor'
cor = {
    'limpa': '\033[m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m'
}

# Exemplo de uso de variáveis para formatação
print(f'{cor["verde"]}Texto em verde{cor["limpa"]}')
print(f'{cor["vermelho"]}Texto em vermelho{cor["limpa"]}')
