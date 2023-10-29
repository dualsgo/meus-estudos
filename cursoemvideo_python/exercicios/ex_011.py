"""Desafio 011 - Pintando Parede (Aula 01 a 07): Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo quecada litro de tinta pinta uma área de 2m**2"""

# Passo 1: Ler a largura e a altura de uma parede - Criamos uma variável para armazenar a altura e outra para armazenar a largura, ambas fornecidas pelo usuário através da função input. Os valores serão digitados em ponto (em centimetros) mas serão convertidos para float
print("""
\033[1;31m P \033[m\033[1;32m I \033[m\033[1;33m N \033[m\033[1;34m T \033[m\033[1;35m A \033[m\033[1;36m N \033[m\033[1;37m D \033[m\033[1;31m O \033[m
""")
print('\033[1mSaiba qual a quantidade de tinta necessária para pintar sua parede!\033[m\n')

altura = float(input('Digite a altura da parede em metros: \n'))
print(f'A altura digitada foi: \033[1;31m{altura:.0f} metros\033[m.\n')
largura = float(input('Digite a largura da parede em metros: \n'))
print(f'A largura digitada foi: \033[1;31m{largura:.0f} metros\033[m.\n')
# Passo 2: Calcular a sua área e a quantidade de tinta necessária para pintá-la - Faremos o cálculo para saber a área em metro quadrado.
area = altura * largura
print(f"""
A sua parede tem \033[1;31m{altura:.2f}m de altura\033[m.
A sua parede tem \033[1;31m{largura:.2f}m de largura\033[m.
A área da sua parede é de \033[1;31m{area:.2f}m²\033[m""")
# Agora que sabemos o metro quadrado faremos o cálculo de quantos litros de tinta serão utilizados.
litros = area / 2

print(f"""
Para pintar toda a sua parede de \033[1;31m{area:.2f}m²\033[m será necessário utilizar \033[1;31m{litros:.1f}L\033[m de tinta.
""")

# Extra - Informar a quantidade de galões de 3.6L ou de 18L que serão necessários. Na própria string usaremos a expressão convertida para int() para desse forma desconsiderar a parte fracionária.

print(f'Você terá que comprar \033[1;31m{int(litros / 3.6)} galões de 3,6L\033[m ou \033[1;32m{int(litros / 18)} galões de 18L\033[1;31m de tinta.')
