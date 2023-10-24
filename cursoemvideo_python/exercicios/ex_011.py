"""Desafio 011 - Pintando Parede (Aula 01 a 07): Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo quecada litro de tinta pinta uma área de 2m**2"""

# Passo 1: Ler a largura e a altura de uma parede - Criamos uma variável para armazenar a altura e outra para armazenar a largura, ambas fornecidas pelo usuário através da função input. Os valores serão digitados em ponto (em centimetros) mas serão convertidos para float
print("""
\033[1;31m P \033[m\033[1;32m I \033[m\033[1;33m N \033[m\033[1;34m T \033[m\033[1;35m A \033[m\033[1;36m N \033[m\033[1;37m D \033[m\033[1;31m O \033[m
""")
print('\033[1mSaiba qual a quantidade de tinta necessária para pintar sua parede!\033[m\n')

altura = float(input('Digite a altura da parede em metros: \n'))
print(f'A altura digitada foi: {altura:.0f} centimetros.\n')
largura = float(input('Digite a largura da parede em metros: \n'))
print(f'A largura digitada foi: {largura:.0f} centimetros.\n')
# Passo 2: Calcular a sua área e a quantidade de tinta necessária para pintá-la - Faremos o cálculo para saber a área em metro quadrado.
area = altura * largura
print(f"""
A sua parede tem {altura:.2f}m de altura.
A sua parede tem {largura:.2f}m de largura.
A área da sua parede é de {area:.2f}m²""")
# Agora que sabemos o metro quadrado faremos o cálculo de quantos litros de tinta serão utilizados.
litros = area / 2

print(f"""
Para pintar toda a sua parede de {area:.2f}m² será necessário utilizar {litros:.1f}L de tinta.
""")
