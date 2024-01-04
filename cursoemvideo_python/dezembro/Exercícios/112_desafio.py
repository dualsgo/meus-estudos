# Exercício Python #112 - Entrada de dados monetários - Aula 00 até 22 - Mundo 3
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
from cursoemvideo_python.dezembro.Exercícios.pacoteexercicios.dado import leia_dinheiro

entrada = input('Digite um valor R$ ').strip()
print(leia_dinheiro(entrada))