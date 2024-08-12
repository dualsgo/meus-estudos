# Exercício Python #107 - Exercitando módulos em Python - Aula 00 até 22 - Mundo 3
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from pacoteexercicios import moeda

valor = moeda.obter_valor_valido('Digite um valor: R$ ')
taxa = moeda.obter_valor_valido(f'Colocar taxa de quantos % nos {moeda.moeda(valor)} - ')/100

# Aumentando
print(f'O valor {moeda.moeda(valor)} aumentado em {taxa:.0%} é {moeda.aumentar(valor, taxa)}')

# Diminuindo
print(f'O valor {moeda.moeda(valor)} diminuído em {taxa:.0%} é {moeda.diminuir(valor, taxa)}')

# Dobrando
print(f'O valor {moeda.moeda(valor)} dobrado é {moeda.dobro(valor)}')

# Dividindo
print(f'O valor {moeda.moeda(valor)} pela metade é {moeda.metade(valor)}')