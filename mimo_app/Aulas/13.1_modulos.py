# MIMO - 13 - Bibbliotecas e módulos
# 13.1 - Módulos

# As classes são uma forma de organizar dados e funcionalidades juntos. Podemos adicionar mais organização ao nosso código com algo chamado módulo. Um módulo é um arquivo Python que contém um conjunto de funcionalidades relacionadas. Por exemplo, podemos ter um módulo chamado math.py que contém funções matemáticas. Podemos ter outro módulo chamado string.py que contém funções relacionadas a strings. Podemos ter outro módulo chamado datetime.py que contém funções relacionadas a datas e horas. E assim por diante.

# Os módulos agrupam classes e dados relacionados e os tornam acessíveis eu um só lugar.

# Alguns módulos estão disponíveis online para as pessoas usarem em seus códigos.

# Python possui alguns módulos integragos. O módulo math fornece dados como o valor de pi.

import math
print(math.pi)  # 3.141592653589793
# O módulo math também fornece funções matemáticas como sqrt() para calcular a raiz quadrada de um número.
print(math.sqrt(25))  # 5.0

# Para usar um módulo usamos a palavra reservada import seguida do nome do módulo.

# Depois de importar um módulo, podemos acessar seus dados e funcionalidades usando a notação de ponto, como math.pi e math.sqrt().

# Podemos descobrir as funcionalidades que um módulo fornece usando a função dir() ou help().

# dir() retorna uma lista de todas as funcionalidades disponíveis em um módulo.
print(dir(math))

# help() retorna uma lista de todas as funcionalidades disponíveis em um módulo, além de informações sobre como usar cada funcionalidade.
print(help(math))

# statistics é outro módulo integrado que fornece funcionalidades para calcular estatísticas. Por exemplo, podemos usar a função mean() para calcular a média de uma lista de números.

import statistics

scores = [85, 93, 45, 87, 93]
mean = statistics.mean(scores)
print(f'Média: {mean}')  # Média: 80.6

# Podemos usar vários módulos diferentes no mesmo arquivo adicionando uma vírgula entre os nomes dos módulos.

# import math, statistics

# As vezes queremos usar apenas partes de um módulo. Podemos fazer isso usando a palavra reservada from.

# from math import pi
# Quando usamos from, não precisamos usar a notação de ponto para acessar as funcionalidades do módulo. Podemos usar a funcionalidade diretamente.

# Podemos modificar o nome do módulo que estamos importando usando a palavra reservada as.

# import statistics as stats
# Isso é útil quando o nome do módulo é muito longo ou quando o nome do módulo entra em conflito com o nome de uma variável que já existe. Isso é chamado de aliasing.

# import math as m