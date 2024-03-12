# MIMO - 13 - Bibliotecas e módulos
# 13.2 - Bibliotecas

# Bibliotecas são coleções de módulos que nos ajudam a economizar tempo na codificação. Pense nisso como uma
# biblioteca de livros. Você pode ir à biblioteca pegar um livro em vez de escrever o livro inteiro. As bibliotecas
# são muito úteis quando você está escrevendo um programa. Você pode usar uma biblioteca para fazer algo que você não quer escrever do zero.

# Muitos módulos constituem uma biblioteca. Usamos math e statistics, que fazem parte da mesma biblioteca.

# Eles fazem parte da The Python Standard Library, que é uma coleção de módulos integrados que vêm com Python. # A biblioteca padrão é instalada com Python, portanto, não precisamos instalá-la separadamente.

# Se quisermos saber mais sobre bibliotecas devemos acessar a documentação oficial do Python.

# Se quisermos lidar com expressoes regulares podemos usar uma biblioteca de processamento de texto. O módulo re fornece funcionalidades para trabalhar com expressões regulares.

# Se quisermos lidar com datas e horas podemos usar uma biblioteca de data e hora. O módulo datetime fornece funcionalidades para trabalhar com datas e horas.

# Para instalar uma nova biblioteca devemos usar o comando pip install seguido do nome da biblioteca.

# pip significar Python Install Package. É um gerenciador de pacotes para Python. Um gerenciador de pacotes é um programa que instala e gerencia bibliotecas e módulos.

# Podemos por exemplo instalar a biblioteca matbplotlib que fornece funcionalidades para criar gráficos.

# Após a instalação podemos importar a biblioteca e usar suas funcionalidades.

from matplotlib import pyplot

# Podemos usar a função plot() para criar um gráfico de linha e a função show() para exibir o gráfico.

# plot() aceita 2 parâmetros: uma lista de valores para o eixo x e uma lista de valores para o eixo y.
# show() não aceita parâmetros.

x = [0, 1]
y = [0, 1]
pyplot.plot(x, y)
pyplot.show()