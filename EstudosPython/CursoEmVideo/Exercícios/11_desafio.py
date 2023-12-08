# Exercício Python #011 - Pintando Parede - Aula 00 até 07 - Mundo 1
# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m².

# Tarefa 1: Ler a altura e a largura de uma parede.
largura = float(input('Digite a largura da parede em metros: '))
print(f'A largura da parede é {largura}m.')
altura = float(input('Digite a altura da parede em metros: '))
print(f'A altura da parede é {altura}m.')
# Tarefa 2: Calcular a área
area = largura * altura
print(f'A área total da parede é de {area}m².')

# Tarefa 3: Calcular a quantidade de tinta necessária.
litro_tinta_por_area = 2
tinta_necessaria = area / litro_tinta_por_area

# Tarefa 4: Mostra o resultado.
print(f'Serão necessários {tinta_necessaria:.2f}L de tinta para pintar sua parede de dimensão {largura}x{altura}!')
